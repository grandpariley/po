# import progressbar

from po.pkg.consts import Constants
from po.pkg.log_level import LogLevel


class ProgressBar:
    @classmethod
    def begin(cls, max_value):
        if Constants.LOG_LEVEL == LogLevel.NONE:
            return
        cls.max_value = max_value
        # cls.bar = progressbar.ProgressBar(maxval=max_value).start()

    @classmethod
    def update(cls, value):
        if Constants.LOG_LEVEL == LogLevel.NONE:
            return
        if value > cls.max_value:
            raise ValueError(str(value) + ' is greater than max value ' + str(cls.max_value))
        # cls.bar.update(value)

    @classmethod
    def end(cls):
        if Constants.LOG_LEVEL == LogLevel.NONE:
            return
        # cls.bar.finish()
