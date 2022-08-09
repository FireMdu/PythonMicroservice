import datetime
import os
import time

from src.schedules.common.schedule_base import SchedulingBase
from src.infrastructure.logger import LogManager

class CuckooSchedule(SchedulingBase):

    def __init__(self):
        SchedulingBase.__init__(self, type(self).__name__, LogManager.new(__name__))

    def exec(self):
       now = datetime.datetime.now()
       os.system('cls')
       print("The clock opens...") 
       clock_says =  ''     
       for i in range(now.hour):
           clock_says += 'Cuckoo '

       print(f"{clock_says}")
       last_run = "N/A" if self.last_run_time is None else self.last_run_time.strftime("%Y-%m-%d %H:%M:%S")
       print(f"The clock closes. Last time it opened was {last_run}")
       time.sleep(2)
