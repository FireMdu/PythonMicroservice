import logging
import sys
import logging.handlers as handlers

from logging import config
from src.common.locations import Locations


class LogManager():

    @staticmethod
    def new(name = 'Default'):

        #TODO: Move config to logging.ini        
        logger = logging.getLogger(name)

        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', 
                                    '%m-%d-%Y %H:%M:%S')

        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(formatter)

        file_name = f'{Locations.root_path()}/logs/app.log'
        file_handler = handlers.RotatingFileHandler(
                file_name, maxBytes=4029,
                backupCount=20)
        
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stdout_handler)
        
        return logger
