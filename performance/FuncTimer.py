from functools import wraps
import time
import pandas as pd

# dictionary of tasks tracing by FuncTimer
tasklist = {}

class FuncTask:
    """
    A task object the FuncTimer is tracing
    task_name (str): name of the task
    interval (float): execution time of the task
    """

    def __init__(self, task_name, interval):
        self.task_name = task_name
        self.frequency = 1
        self.total_interval = interval
    
    def increment(self, interval):
        """
        Update the statistics when a new task is called
        interval (float): execution time of the task
        """
        self.frequency += 1
        self.total_interval += interval
    
    def getAverageTime(self):
        """
        Get the average runtime for the task
        """
        return self.total_interval / self.frequency

class FuncTimer(object):
    """
    A timer that helps trace the execution time
    task_name (str) : name of the task
    """

    def __init__(self, task_name):
        self.task_name = task_name
    
    def __call__(self, wrappedCall):
        @wraps(wrappedCall)
        def wrapCall(*args, **kwargs):
            try:
                self.before()
                r = wrappedCall(*args, **kwargs)
            finally:
                self.after()
            return r
        return wrapCall

    def before(self):
        self.start_time = time.time()
        return self

    def after(self):
        self.end_time = time.time()
        self.interval = self.end_time - self.start_time
        if self.task_name not in tasklist.keys():
            tasklist[self.task_name] = FuncTask(self.task_name, self.interval)
        else:
            tasklist[self.task_name].increment(self.interval)


    # def __enter__(self):
    #     self.start_time = time.time()
    #     return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.end_time = time.time()
    #     self.interval = self.end_time - self.start_time
    #     if self.task_name not in tasklist.keys():
    #         tasklist[self.task_name] = FuncTask(self.task_name, self.interval)
    #     else:
    #         tasklist[self.task_name].increment(self.interval)

    @staticmethod
    def printStat():
        """
        Print the average runtime statistics
        """
        print 'PERFORMANCE METRICS:'
        print 60*'-'
        print '*** Average Runtime ***'
        print 'Task Name             \t Average Exec Time (s)      \t Number of Executions'
        for k, v in tasklist.items():
            print '{:40s} {:12.8f}  {:8d}'.format(k, v.getAverageTime(), v.frequency)
        print 60*'-'



