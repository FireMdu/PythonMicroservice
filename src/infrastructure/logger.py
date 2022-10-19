import logging
import logging.handlers as handlers

from logging.handlers import TimedRotatingFileHandler
from src.infrastructure.locations import Locations
from src.infrastructure.singleton_decorator import Singleton
from enum import Enum


class RollingFileMethod(Enum):
    ByMaxSize = 1
    Daily = 2


class LogManager(metaclass=Singleton):
    _logger = None
    _name = 'app'
    _rolling_file_method = RollingFileMethod.ByMaxSize
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", '%m-%d-%Y %H:%M:%S')

    def __init__(self) -> None:
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.INFO)  # Only log entries from this level or higher

        self._logger.addHandler(self.create_console_handler())
        if self._rolling_file_method == RollingFileMethod.ByMaxSize:
            self._logger.addHandler(self.create_rolling_file_handler_by_size(self._name))

        if self._rolling_file_method == RollingFileMethod.Daily:
            self._logger.addHandler(self.create_rolling_file_handler_daily(self._name))

    @property
    def logger(self) -> logging.Logger:
        return self._logger

    def create_rolling_file_handler_daily(self, file_name):
        log_file_daily_path = f'{Locations.root_path()}/logs/{file_name}.log'
        handler = TimedRotatingFileHandler(
            filename=log_file_daily_path,
            when="D",  # D: daily | H: hourly | M: minutes
            interval=1,  # Every X days/hours/minutes
            backupCount=20)  # For X number of files
        handler.setFormatter(self.formatter)
        handler.setLevel(logging.INFO)
        handler.suffix = "%Y-%m-%d_%H_%M"
        return handler

    def create_rolling_file_handler_by_size(self, file_name):
        log_file_size_path = f'{Locations.root_path()}/logs/{file_name}.log'
        handler = handlers.RotatingFileHandler(
                log_file_size_path,
                maxBytes=10000000,  # Maximum file size
                backupCount=20)  # For X number of files
        handler.setFormatter(self.formatter)
        handler.setLevel(logging.INFO)
        return handler

    @staticmethod
    def create_console_handler():
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        return handler
