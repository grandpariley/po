import datetime, os, gc


class Log:
    context = ""

    @classmethod
    def log(cls, obj, context=None, override=False):
        if not (os.environ['DEBUG'] or override):
            return
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
        # FIXME this is so gross
        gc.collect()

    @classmethod
    def newline(cls):
        if not os.environ['DEBUG']:
            return
        print()