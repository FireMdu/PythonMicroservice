from cmath import log
import logging
import os
import logging.handlers as handlers
import logging
import re

from logging.handlers import TimedRotatingFileHandler
from logging import config
from src.common.locations import Locations
from src.common.singleton_decorator import Singleton

class LogManager(metaclass=Singleton):
        _logger = None
        
        @property
        def logger(self) -> logging.Logger:
                return self._logger

        def __init__(self) -> None:
                print('Initializing logging')

                # Main logger
                self._logger = logging.getLogger()
                self._logger.setLevel(logging.INFO)

                formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", '%m-%d-%Y %H:%M:%S')

                # ============ Daily Rolling File Handler ============        
                log_file_daily_path = f'{Locations.root_path()}/logs/daily_app.log'
                file_handler_daily = TimedRotatingFileHandler(
                        filename=log_file_daily_path,
                        when="D",  # D: daily | H: hourly | M: minutes
                        interval=1, # Every X days/hours/minutes
                        backupCount=20) # For X number of files
                file_handler_daily.setFormatter(formatter)
                file_handler_daily.setLevel(logging.INFO)
                file_handler_daily.suffix = "%Y-%m-%d_%H_%M"
                # file_handler_daily.extMatch = re.compile(r"^\d{8}$")

                self._logger.addHandler(file_handler_daily)                

                # ============ Rolling by Size File Handler ============
                log_file_size_path = f'{Locations.root_path()}/logs/size_app.log'
                file_handler_size = handlers.RotatingFileHandler(
                        log_file_size_path, 
                        maxBytes=10000000, # Maximum file size
                        backupCount=20) # For X number of files
                file_handler_size.setFormatter(formatter)
                file_handler_size.setLevel(logging.INFO)

                self._logger.addHandler(file_handler_size)

                print('Logging initiated')