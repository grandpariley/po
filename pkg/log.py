import datetime


class Log:
    debug_mode = False
    context = ""

    @classmethod
    def log(cls, obj, context=None):
        if context is not None:
            cls.context = context
        print(str(datetime.datetime.now()) +
              " : " + cls.context + " : " + str(obj))

    @classmethod
    def begin_debug(cls, context):
        cls.context = str(context)

    @classmethod
    def end_debug(cls):
        cls.context = ""

    @classmethod
    def newline(cls):
        print()