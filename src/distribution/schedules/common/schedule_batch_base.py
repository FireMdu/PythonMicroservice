import os

from abc import ABC, abstractmethod
from src.distribution.schedules.common.schedule_base import SchedulingBase
from src.infrastructure.stopwatch import Stopwatch
from src.infrastructure.logger import LogManager
from src.infrastructure.stopwatch import Stopwatch

logger = LogManager().logger

class BatchScheduleBase(SchedulingBase):
    _batch_size = None
    _batch = None

    def __init__(self, batch_size, name):
        SchedulingBase.__init__(self, name)
        self._batch_size = batch_size
        self.stopwatch = Stopwatch()

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

        count = 0
        succeeded = 0
        failed = 0
        
        for item in self._batch:
            count += 1

            try:
                stopwatch_item = Stopwatch().start()
                self.process_item(item)      
                succeeded += 1
                logger.info(f'Completed item [{count}/{size}] for {self.name} in {stopwatch_item.stop_success().elapsed_time_in_seconds()}s')  
            except Exception as ex:
                logger.error(f"Error {ex.__class__} occurred for [{self.name}] item [{count}/{size}] after {stopwatch_item.stop_failure().elapsed_time_in_seconds()}s while fetching the next batch. Details: {ex}")
                failed += 1
                

        logger.info(f'Batch for {self.name} done. [{count}] items processed in {self.stopwatch.stop_success().elapsed_time_in_seconds()}s (Succeeded=[{succeeded}] Failed=[{failed}] Remaining=[{remaining_items - succeeded}]).')
        logger.info('')
