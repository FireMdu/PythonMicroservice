from enum import Enum
from threading import Thread, Lock

class ThreadType(Enum):
    Unknown = 0
    Scheduler = 1
    WebApp = 2
    API = 3

class ThreadManager:
    threads = dict()
    mutex = Lock()

    def add_update_thread(self, type, thread):
        self.mutex.acquire()        
        self.threads[type] = thread
        self.mutex.release()    

    def get_thread_by_type(self, type):
        return self.threads[type]

    def has_active_threads(self):
        for key in self.threads:            
            if self.threads[key].is_alive():
                return True

        return False

