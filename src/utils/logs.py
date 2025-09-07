import logging
import time
import functools
from src.initialize.init import ENV


def set_up_log(logname):
    """
    Create a logging file

    logname = __name__

    - Allows toggling logging on/off via
    """

    # Determine logging level based on the environment variable
    if ENV.TURN_ON_LOGGING:
        log_level_str = getattr(ENV, "LOG_LEVEL", "DEBUG")
        log_level = getattr(ENV, log_level_str, logging.DEBUG)
    else:
        log_level = logging.CRITICAL + 1 # Effectively disables logging

    logging.basicConfig(level=log_level)
    logger = logging.getLogger(logname)

    # Create a file as handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def time_it(unit=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            start_time = time.time()
            try:
                result = func(*args, **kwargs)
            finally:
                end_time = time.time()
                execution_time = end_time - start_time
                class_name = func.__qualname__.split('.')[0] if '.' in func.__qualname__ else 'Global'
                print(f"{unit if unit else ''} {class_name}.{func.__name__}, time cost: {execution_time:.6f}s")
            return result
        return wrapper
    return decorator