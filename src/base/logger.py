import datetime
import errno
import logging
import os

from config import BaseConfig


def create_logger(name='PYTHON_3', level='DEBUG'):
    logger_ = logging.getLogger() if name is None else logging.getLogger(name)
    logger_.setLevel(level)
    format_ = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(format_)
    log_file = _create_log_file()
    log_file = logging.FileHandler(log_file)
    log_file.setFormatter(formatter)
    log_file.setLevel(level)
    logger_.addHandler(log_file)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger_.addHandler(console_handler)
    return logger_


def _create_log_file():
    cur_time_stamp = int(datetime.datetime.today().timestamp())
    filename = str(cur_time_stamp) + "_automation_test.log"
    path = BaseConfig.LOGS
    message = " --- LOGGING STARTED: "
    cur_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if not os.access(path, os.F_OK) or not os.path.isdir(path) or not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(path)
            with open(path + filename, "w+") as f:
                f.write(message + cur_date)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    with open(path + filename, "a") as f:
        f.write(cur_date + message + "\n")
    return path + filename


logger = create_logger()