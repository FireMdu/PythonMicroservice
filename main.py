from src.infrastructure.logger import LogManager
from src.schedules.scheduler import Scheduler

logger = LogManager.new()

def main():
    logger.info('Starting microservice...')

    # Starting Schedules
    Scheduler().start()


main()

