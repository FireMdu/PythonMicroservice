import asyncio

from src.distribution.schedules.common.schedule_manager import ScheduleManager
from src.distribution.schedules.common.overview_schedule import OverviewSchedule
from src.distribution.schedules.cuckoo_clock_schedule import CuckooSchedule
from src.distribution.schedules.queue_batch_schedule import QueueBatchSchedule

class Scheduler():
    schedule_manager = ScheduleManager()
    thread_manager = None

    cuckoo = CuckooSchedule()
    overview = OverviewSchedule()
    queue_batch = QueueBatchSchedule(20)

    async def register_schedules(self):
        asyncio.ensure_future(self.cuckoo.start(self.schedule_manager, 12))
        asyncio.ensure_future(self.overview.start(self.schedule_manager, 5))
        asyncio.ensure_future(self.queue_batch.start(self.schedule_manager, 5))

    def start(self, thread_manager):
        self.thread_manager = thread_manager
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            asyncio.ensure_future(self.register_schedules())
            loop.run_forever()
        finally:
            loop.close()



