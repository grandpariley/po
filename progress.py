import progressbar

from pkg.log import Log


class ProgressBar:
    @classmethod
    def begin(cls, max_value):
        cls.max_value = max_value
        cls.bar = progressbar.ProgressBar(maxval=max_value).start()

    @classmethod
    def update(cls, value):
        if value > cls.max_value:
            raise ValueError(str(value) + ' is greater than max value ' + str(cls.max_value))
        cls.bar.update(value)

    @classmethod
    def end(cls):
        cls.bar.finish()
