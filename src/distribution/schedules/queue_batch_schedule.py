import random
import time

from src.distribution.schedules.common.schedule_batch_base import BatchScheduleBase
from src.infrastructure.logger import LogManager

logger = LogManager().logger

class QueueBatchSchedule(BatchScheduleBase):

    def __init__(self, batch_size):
        BatchScheduleBase.__init__(self, batch_size, type(self).__name__)        

    # Just for testing purposes
    def get_random_batch_size(self):
        value = random.randint(1, 3)

        switcher = {
            1:  15,
            2:  45,
            3:  5,
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
        print(f'Item processed. Value [{item}]')
        time.sleep(0.05)

