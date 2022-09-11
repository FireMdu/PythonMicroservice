import os

from src.distribution.schedules.common.schedule_base import SchedulingBase
from src.infrastructure.logger import LogManager

class OverviewSchedule(SchedulingBase):

    logger = LogManager().logger

    def __init__(self):
        SchedulingBase.__init__(self, type(self).__name__)

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
            last_run = "N/A" if schedule.stopwatch.last_success_time is None else schedule.stopwatch.last_success_time.strftime("%Y-%m-%d %H:%M:%S")
            last_duration = "N/A" if schedule.stopwatch.last_success_time is None else str(round(schedule.stopwatch.elapsed_time_in_seconds(), 2))

            print(f"[{schedule.name}]: Active, last ran at {last_run} for {last_duration}s")
        print()

        