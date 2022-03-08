import time
import logging
from functools import wraps


def my_timer(original_function):
    @wraps(original_function)
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=original_function(*args,**kwargs)
        t2=time.time()
        print(f'{original_function.__name__} ran in {t2-t1} sec')
        return result
    return wrapper



logging.basicConfig(filename='example.log', level=logging.INFO)

def my_logger(func):
    @wraps(func)
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def p():
    print('hi')
