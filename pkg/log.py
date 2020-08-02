import datetime

class Log:
    debug_mode = False
    context = ""
    
    @classmethod
    def log(cls, obj):
        if cls.debug_mode:
            print(str(datetime.datetime.now()) + " : " + cls.context + " : " + str(obj))
    
    @classmethod
    def begin_debug(cls, context):
        cls.debug_mode = True
        cls.context = str(context)
    
    @classmethod
    def end_debug(cls):
        cls.debug_mode = False
        cls.context = ""