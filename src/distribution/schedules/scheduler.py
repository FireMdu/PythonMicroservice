import asyncio

from src.distribution.schedules.common.schedule_manager import ScheduleManager
from src.distribution.schedules.common.overview_schedule import OverviewSchedule
from src.distribution.schedules.cuckoo_clock_schedule import CuckooSchedule
from src.distribution.schedules.queue_batch_schedule import QueueBatchSchedule

class Scheduler():
    schedule_manager = ScheduleManager()

    cuckoo = CuckooSchedule()
    overview = OverviewSchedule()
    queue_batch = QueueBatchSchedule(20)

    def register_schedules(self, future):
        asyncio.ensure_future(self.cuckoo.start(self.schedule_manager, 12, future))
        asyncio.ensure_future(self.overview.start(self.schedule_manager, 5, future))
        asyncio.ensure_future(self.queue_batch.start(self.schedule_manager, 5, future))

    def start(self):
        loop = asyncio.get_event_loop()
        future = asyncio.Future()

        self.register_schedules(future)

        try:
            loop.run_forever()
        finally:
            loop.close()



