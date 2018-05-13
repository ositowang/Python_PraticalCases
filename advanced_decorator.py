from functools import wraps
import time
import logging
from random import randint


# Decorator with actionable variables

def warn(timeout):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            used = time.time() - start
            if used > timeout:
                msg = '"%s": %s > %s' % (func.__name__, used, timeout)
                logging.warning(msg)
            return res

        def settimeout(k):
            nonlocal timeout
            timeout = k

        wrapper.setTimeout = settimeout

        return wrapper

    return decorator


@warn(1.5)
def test():
    print("in test")
    while randint(0, 1):
        time.sleep(0.5)


for _ in range(30):
    test()
