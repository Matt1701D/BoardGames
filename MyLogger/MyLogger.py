import logging

class MyLogger(logging.getLoggerClass()):

    logFileName = "BoardGames.log"
    logFileMode = "w"
    logName = "BoardGames"
    logLevel = "INFO"

    @classmethod
    def getMyLogger(cls, **kwargs):

        # setup logger
        logFileName = cls.logFileName if kwargs.get("logFileName", None) == None else kwargs["logFileName"] 
        logFileMode = cls.logFileMode if kwargs.get("logFileMode", None) == None else kwargs["logFileMode"] 
        logName = cls.logName if kwargs.get("logName", None) == None else kwargs["logName"] 
        logLevel = cls.logLevel if kwargs.get("logLevel", None) == None else kwargs["logLevel"] 

        # create logger
        cls.myLog = logging.getLogger(logName)
        cls.myLog.setLevel(logLevel)

        # create formatter
        myLogFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # create file handler for logger.
        myLogFH = logging.FileHandler(logFileName, logFileMode)
        myLogFH.setLevel(logLevel)
        myLogFH.setFormatter(myLogFormat)

        cls.myLog.addHandler(myLogFH)

    @classmethod
    def log(cls,msg):
        strOutput = msg
        cls.myLog.info(strOutput)

    # DEPRECATED - used below within each method to log
    #MyLogger.TraceEnter(type(self).__qualname__ +"."+sys._getframe().f_code.co_name)
    @classmethod
    def TraceEnter(cls,msg):
        strOutput = "Entering " + msg
        cls.myLog.info(strOutput)

    @classmethod
    def TraceExit(cls,msg):
        strOutput = "Exiting " + msg
        cls.myLog.info(strOutput)

    def log_decorator(func):
        def wrapper(*args,**kwargs):
            funcName = func.__qualname__ if func.__qualname__ else func.__name__
            with TraceLog(funcName):
                return func(*args,**kwargs)
        return wrapper

class TraceLog(object):
    def __init__(self, funcName):
        self.funcName = funcName

    def __enter__(self):
        strOutput = "Entering " + self.funcName
        MyLogger.log(strOutput)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        strOutput = "Exiting " + self.funcName
        MyLogger.log(strOutput)


