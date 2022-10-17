import time
from threading import Thread

from src.infrastructure.logger import LogManager
from src.distribution.schedules.scheduler import Scheduler
from src.distribution.api.api_manager import AppManager
from src.infrastructure.thread_manager import ThreadManager, ThreadType

logger = LogManager().logger


def main():
    logger.info('Starting microservice...')

    thread_manager = ThreadManager()
    
    # Start Scheduler on its own thread
    scheduler = Scheduler()
    scheduler_thread = Thread(target=scheduler.start,args=(thread_manager,))    
    thread_manager.add_update_thread(thread_type=ThreadType.Scheduler, thread=scheduler_thread)
    scheduler_thread.start()

    # Start API on its own Thread
    app_manager = AppManager()
    api_thread = Thread(target=app_manager.start, args=(thread_manager,))
    thread_manager.add_update_thread(thread_type=ThreadType.API, thread=api_thread)
    api_thread.start()

    while thread_manager.has_active_threads():
        # TODO: check thread health and recover if necessary
        time.sleep(5)
    logger.info("Microservice stopped")


if __name__ == '__main__':
    main()
