import threading

class ScheduleManager():
    schedules = dict()
    lock = None

    def __init__(self) -> None:
        self.lock =  threading.Lock()

    def add_schedule(self, key, schedule):
        self.lock.acquire()

        try:
            if key in self.schedules:
                raise Exception(f"Cannot add schedule [{key}] one is already running.")
            self.schedules[key] = schedule
        finally:
            self.lock.release()

    def add_update_schedule(self, key, schedule):
        self.lock.acquire()

        try:
            self.schedules[key] = schedule
        finally:
            self.lock.release()

    def remove_schedule(self, key):
        self.lock.acquire()

        try:
            del self.schedules[key]
        finally:
            self.lock.release()

