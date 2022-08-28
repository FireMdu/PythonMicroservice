from src.infrastructure.logger import LogManager
from src.distribution.schedules.scheduler import Scheduler
from src.distribution.api.api_manager import AppManager

logger = LogManager().logger

def main():
    logger.info('Starting microservice...')

    # Starting Schedules
    # Scheduler().start()
    AppManager().start()


main()

