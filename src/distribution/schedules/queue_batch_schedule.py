import random
import time

from src.distribution.schedules.common.schedule_batch_base import BatchScheduleBase
from src.infrastructure.logger import LogManager

logger = LogManager().logger

class QueueBatchSchedule(BatchScheduleBase):

    def __init__(self, batch_size):
        BatchScheduleBase.__init__(self, 
            batch_size = batch_size, 
            name = type(self).__name__, 
            concurrent_threads = 3, 
            thread_queue_size = 10)        

    # Just for testing purposes
    def get_random_batch_size(self):
        value = random.randint(1, 5)

        switcher = {
            1:  15,
            2:  45,
            3:  5,
            4:  60,
            5:  125
        }

        return switcher.get(value, 0)
    
    def count_items_to_process(self):
        items = self.get_random_batch_size()
        return items

    def fetch_next_batch(self, size):
        batch = []
        for value in range(1, size + 1):            
            batch.append(value)

        return batch

    def process_item(self, item):
        # Placeholder for item logic
        time.sleep(0.05)

