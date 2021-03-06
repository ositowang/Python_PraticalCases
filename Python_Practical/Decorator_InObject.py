from time import localtime, time, strftime, sleep
import logging
from random import choice


class CallingInfo(object):
    def __init__(self, name):
        log = logging.getLogger(name)
        log.setLevel(logging.INFO)
        fh = logging.FileHandler(name + ".log")
        log.addHandler(fh)
        log.info("Start".center(50, "-"))
        self.log = log
        self.formatter = "%(func)s ->[%(time)s-%(used)s- %(ncalls)s]"

    def info(self, func):
        def wrapper(*args, **kwargs):
            wrapper.ncalls += 1
            lt = localtime()
            start = time()
            res = func(*args, **kwargs)
            used = time() - start
            info = {}
            info["func"] = func.__name__
            info["time"] = strftime("%x %X", lt)
            info["used"] = used
            info["ncalls"] = wrapper.ncalls
            msg = self.formatter % info
            self.log.info(msg)
            return res

        return wrapper

    def set_formatter(self, formatter):
        self.formatter = formatter

    def turn_on(self):
        self.log.setLevel(logging.INFO)

    def turnoff(self):
        self.log.setLevel(logging.WARN)


cinfo1 = CallingInfo("mylog1")
cinfo2 = CallingInfo("mylog2")


@cinfo1.info
def f():
    print("in f")


@cinfo1.info
def g():
    print("in g")


@cinfo2.info
def h():
    print("in h ")


for _ in range(30):
    choice([f, g, h])
    sleep(choice([0.5, 1, 1.5]))
