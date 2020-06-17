import inspect
import logging


def custom_logger(log_level=logging.DEBUG):
    # gets the name of the class or method
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # by default, log all messages
    logger.setLevel(logging.DEBUG)

    # file_handler = logging.FileHandler("{0}.log".format(logger_name), mode='w')
    file_handler = logging.FileHandler("automation.log", mode='w') # mode='a' to append
    # file_handler = logging.StreamHandler()
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
