import datetime
import gc
import os

from po.pkg.consts import Constants
from po.pkg.log_level import LogLevel


class Log:
    context = ''

    @classmethod
    def log(cls, obj, context=None):
        if Constants.LOG_LEVEL == LogLevel.NONE:
            return
        if context is None and cls.context is None:
            cls.context = os.getenv('LOG_LEVEL')
        elif context is not None:
            cls.context = context
        print(str(datetime.datetime.now()) + ' : ' + cls.context + ' : ' + str(obj))

    @classmethod
    def begin_debug(cls, context):
        cls.context = str(context)

    @classmethod
    def end_debug(cls):
        cls.context = ''
        gc.collect()

    @classmethod
    def newline(cls):
        if Constants.LOG_LEVEL != LogLevel.NONE:
            print()
