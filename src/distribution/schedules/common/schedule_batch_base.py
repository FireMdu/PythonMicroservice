import os
import time

from enum import Enum
from abc import ABC, abstractmethod
from src.distribution.schedules.common.schedule_base import SchedulingBase
from src.infrastructure.stopwatch import Stopwatch
from src.infrastructure.logger import LogManager
from src.infrastructure.stopwatch import Stopwatch
from threading import Thread, Lock

logger = LogManager().logger

class Outcome(Enum):
    Unkown = 0
    Pending = 1
    Success = 2
    Failure = 3

class Counters():
    pending = 0
    successfull = 0
    failed = 0
    remaining = 0
    processed = 0
    total_processing_time = 0

    def __init__(self, pending, remaining) -> None:
        self.pending = pending
        self.remaining = remaining

class BatchScheduleBase(SchedulingBase):
    _batch_size = None
    _batch = None
    _concurrent_threads = None
    _thread_queue_size = None
    _mutex = Lock()

    def __init__(self, batch_size, name, concurrent_threads = 1, thread_queue_size = 10):
        SchedulingBase.__init__(self, name)
        self._batch_size = batch_size
        self.stopwatch = Stopwatch()
        self._concurrent_threads = concurrent_threads
        self._thread_queue_size = thread_queue_size

    def get_queue_batch(self, number_of_items):
        queue = []

        count_queue_added = 0
        while len(self._batch) > 0 and count_queue_added < number_of_items:
            count_queue_added += 1
            item_to_move = self._batch.pop(0)
            queue.append(item_to_move)

        return queue

    def process_queue_in_seperate_thread(self, thread_queue, thread_number, counters):   
        count_items = 0
        stopwatch_thread = Stopwatch().start()

        for item in thread_queue:
            count_items += 1
            outcome = Outcome.Unkown

            try:
                stopwatch_item = Stopwatch().start()
                self.process_item(item)      
                outcome = Outcome.Success
                logger.info(f'Completed item [{thread_number}.{count_items}/{counters.pending}] for {self.name} in {stopwatch_item.stop_success().elapsed_time_in_seconds()}s')  
            except Exception as ex:
                logger.error(f"Error {ex.__class__} occurred for [{self.name}] item [{thread_number}.{count_items}/{counters.pending}] after {stopwatch_item.stop_failure().elapsed_time_in_seconds()}s while fetching the next batch. Details: {ex}")
                outcome = Outcome.Failure

            # Update counters
            self._mutex.acquire()
            if (outcome == Outcome.Success):
                counters.successfull += 1
            elif(outcome == Outcome.Failure):
                counters.failure += 1
            counters.pending -= 1
            counters.remaining -= 1
            counters.processed += 1
            counters.total_processing_time += stopwatch_thread.stop_success().elapsed_time_in_seconds()
            self._mutex.release()

    @abstractmethod
    def count_items_to_process(self):
        return None

    @abstractmethod
    def fetch_next_batch(self, batch_size):
        pass

    @abstractmethod
    def process_item(self, item):
        pass

    def exec(self):
        remaining_items = 0
        self.stopwatch.start() 

        try:            
            remaining_items = self.count_items_to_process() 
        except Exception as ex:
            logger.error(f"Error {ex.__class__} occurred for [{self.name}] while retrieving remaining items. Details: {ex}")  
            remaining_items = 0
          
        size = self._batch_size if self._batch_size < remaining_items else remaining_items

        stopwatch_get_batch = Stopwatch().start()
        try:            
            self._batch = self.fetch_next_batch(size)
            stopwatch_get_batch.stop_success()

            batch_size = len(self._batch)
            if batch_size > 0:
                logger.info(f'Fetched a new batch for {self.name} of {batch_size} items in {stopwatch_get_batch.elapsed_time_in_seconds()}s')
        except Exception as ex:
            logger.error(f"Error {ex.__class__} occurred for [{self.name}] while fetching the next batch after {stopwatch_get_batch.stop_failure().elapsed_time_in_seconds()}s. Details: {ex}")
            self._batch = []  

        if self._batch is None or len(self._batch) == 0:
            return
            
        if not isinstance(self._batch, list):
            raise ValueError(f'Did not return a valid list of items to be processed. List or None expected but {self._batch} was given.')

        os.system('cls')
        logger.info(f'Starting a new batch of [{size}] for [{self.name}] out of the remaining [{remaining_items}] items')

        counters = Counters(size, remaining_items)

        thread_count = 0
        empty_batch = (size == 0)
        threads = []

        while not empty_batch:
            thread_count += 1

            thread_queue = self.get_queue_batch(self._thread_queue_size)
            thread = Thread(target=self.process_queue_in_seperate_thread,args=(thread_queue, thread_count, counters))
            
            empty_batch = (len(self._batch) == 0)
            threads.append(thread)
            thread.start()

            logger.info(f'Added a thread to process batch [{len(threads)}/{self._concurrent_threads}]')

            while (not empty_batch and len(threads) == self._concurrent_threads):
                time.sleep(2)

                for i in range(len(threads)-1, -1, -1):
                    thread_iterate = threads[i]
                    if not thread_iterate.is_alive():                        
                        threads.remove(thread_iterate)
                        logger.info(f'Removed completed thread position [{i}]. Threads in use [{len(threads)}/{self._concurrent_threads}]')        


        # Wait for all threads to complete
        for thread in threads:
            thread.join()                       

        logger.info(f'Batch for {self.name} done. [{counters.successfull + counters.failed}] items processed in {self.stopwatch.stop_success().elapsed_time_in_seconds()}s (Succeeded=[{counters.successfull}] Failed=[{counters.failed}] Remaining=[{counters.remaining}]) {counters.total_processing_time - self.stopwatch.stop_success().elapsed_time_in_seconds()}s gain with parallelism.')
        logger.info('')
        
        if (size != counters.processed or (counters.successfull + counters.failed) != counters.processed):
            logger.error(f'Batch for {self.name} failed post run counts. Expected [Batch Size-{size}] == [Processed={counters.processed}] and [Success-{counters.successfull} + Failed-{counters.failed}] == [Processed={counters.processed}]')
