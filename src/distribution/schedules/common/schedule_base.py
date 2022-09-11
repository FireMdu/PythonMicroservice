import asyncio
import traceback
import time

from datetime import datetime
from abc import ABC, abstractmethod
from src.infrastructure.stopwatch import Stopwatch
from src.infrastructure.logger import LogManager
from src.infrastructure.stopwatch import Stopwatch

logger = LogManager().logger

class SchedulingBase(ABC):    
    _is_active = False
    schedule_manager = None
    stopwatch = None
    # last_run_time = None
    # last_run_duration = None
    skipped_counter = None
    name = None

    def __init__(self, name):        
        self.name = name
        self.stopwatch = Stopwatch()

    @abstractmethod # Implimented in the derived class
    def exec(self):
        pass    
 
    @asyncio.coroutine
    ## This starts an schedule that will based on intervals execute the next one
    def start(self, schedule_manager, frequency_in_seconds, future):
        
        try:
            logger.info(f"Starting schedule {self.name}.")
            if (self.schedule_manager is None):
                self.schedule_manager = schedule_manager

            self.schedule_manager.add_schedule(self.name, self)
            self._is_active = True

            while self._is_active:
                self.stopwatch.start()

                try:
                    self.exec()

                    self.stopwatch.stop_success()                

                    logger.info(f'Completed schedule for {self.name} in {self.stopwatch.elapsed_time_in_seconds()}s')
                except Exception as ex:
                    logger.error(f"Error {ex.__class__} occurred for [{self.name}] after {self.stopwatch.stop_failure().elapsed_time_in_seconds()}s while executing schedule. Details: {ex}") 

  
                yield from asyncio.sleep(frequency_in_seconds)

            logger.info(f"Schedule {self.name} is now stopping")
            self.stop_schedule()

        except Exception as ex:
            logger.error(f"Error {ex.__class__} occurred for [{self.name}]. Details: {ex}") 
            raise # re-throw after writing error to screen        

    def stop(self):
        self._is_active = False
        logger.info(f"Stopping [{self.name}]...")        
        self.schedule_manager.remove_schedule(self.name)


