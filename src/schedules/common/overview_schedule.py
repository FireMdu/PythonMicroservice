import os

from src.schedules.common.schedule_base import SchedulingBase
from src.infrastructure.logger import LogManager

class OverviewSchedule(SchedulingBase):

    def __init__(self):
        SchedulingBase.__init__(self, type(self).__name__, LogManager.new(__name__))

    def exec(self):
        os.system("cls")
        print()
        print("=====================================================")
        print("===============  Running Schedules ==================")
        print("=====================================================")

        for schedule_key in self.schedule_manager.schedules:
            # Ignore the overview schedule
            if schedule_key == type(self).__name__:
                continue

            schedule = self.schedule_manager.schedules[schedule_key]
            last_run = "N/A" if schedule.last_run_time is None else schedule.last_run_time.strftime("%Y-%m-%d %H:%M:%S")
            last_duration = "N/A" if schedule.last_run_duration is None else str(round(schedule.last_run_duration, 2))

            print(f"[{schedule.name}]: Active, last ran at {last_run} for {last_duration}s")
        print()

        