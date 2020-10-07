import os
import logging
from logging.handlers import TimedRotatingFileHandler
import time

from vlt_path import get_path

path = get_path()
log_path = os.path.join(path, 'log')  # 存放log文件的路径


class Logger(object):
    def __init__(self, logname='autotest'):
        logdir = os.path.dirname(log_path)
        if not os.path.isdir(logdir):
            os.mkdir(logdir)
        self.logger = logging.getLogger(logname)
        logging.root.setLevel(logging.INFO)
        self.log_file_name = '{}.logs'.format(time.strftime('%Y_%m_%d', time.localtime(time.time())))  # 日志文件的名称
        self.backup_count = 10  # 最多存放日志的数量
        # 日志输出级别
        self.console_output_level = logging.DEBUG
        self.file_output_level = 'DEBUG'
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] %(pathname)s =>%(lineno)d 【%(levelname)s】:%(message)s')   #

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, self.log_file_name), when='D',
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()



# %(name)s            Name of the logger (logging channel)
# %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
#                     WARNING, ERROR, CRITICAL)
# %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
#                     "WARNING", "ERROR", "CRITICAL")
# %(pathname)s        Full pathname of the source file where the logging
#                     call was issued (if available)
# %(filename)s        Filename portion of pathname
# %(module)s          Module (name portion of filename)
# %(lineno)d          Source line number where the logging call was issued
#                     (if available)
# %(funcName)s        Function name
# %(created)f         Time when the LogRecord was created (time.time()
#                     return value)
# %(asctime)s         Textual time when the LogRecord was created
# %(msecs)d           Millisecond portion of the creation time
# %(relativeCreated)d Time in milliseconds when the LogRecord was created,
#                     relative to the time the logging module was loaded
#                     (typically at application startup time)
# %(thread)d          Thread ID (if available)
# %(threadName)s      Thread name (if available)
# %(process)d         Process ID (if available)
# %(message)s         The result of record.getMessage(), computed just as
#                     the record is emitted
