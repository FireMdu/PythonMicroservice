from datetime import datetime
from multiprocessing.resource_sharer import stop
import time

from src.distribution.schedules.common.schedule_base import SchedulingBase
from src.infrastructure.logger import LogManager

logger = LogManager().logger

class CuckooSchedule(SchedulingBase):

    def __init__(self):
        SchedulingBase.__init__(self, type(self).__name__)

    def exec(self):
        print("The clock opens...") 
        clock_says =  ''     
        
        for i in range(datetime.now().hour):
            clock_says += 'Cuckoo '

        print(f"{clock_says}")

        print(f"The clock closes. Last time it opened was {self.stopwatch.get_last_successfull_run_time()}")
        time.sleep(2)
