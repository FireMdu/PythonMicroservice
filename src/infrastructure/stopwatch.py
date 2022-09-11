from datetime import datetime

class Stopwatch:
    last_success_time = None
    start_time = None
    end_time = None
    has_error = None

    def start(self):
        self.start_time = datetime.now()
        return self

    def stop_success(self):
        self.end_time = datetime.now()
        self.last_success_time = self.start_time
        self.has_error = False
        return self

    def stop_failure(self):
        self.end_time = datetime.now()
        self.has_error = True
        return self
    
    def elapsed_time_in_seconds(self):
        return (self.end_time - self.start_time).total_seconds()

    def get_last_successfull_run_time(self):
        return "N/A" if self.last_success_time is None else self.last_success_time.strftime("%Y-%m-%d %H:%M:%S")