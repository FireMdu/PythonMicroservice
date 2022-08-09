from src.infrastructure.logger import LogManager
from src.schedules.scheduler import Scheduler

logger = LogManager().logger

def main():
    logger.info('Starting microservice...')

    # Starting Schedules
    Scheduler().start()


main()

