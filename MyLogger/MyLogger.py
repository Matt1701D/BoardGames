import logging, functools
from time import perf_counter_ns
from MyLogger.MyExceptions import *

class MyLogger(logging.getLoggerClass()):

    logFileName = "BoardGames.log"
    logFileMode = "w"
    logName = "BoardGames"
    logLevel = "INFO"
    myLog = None

    @classmethod
    def getMyLogger(cls, **kwargs):
        if cls.myLog is None:
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
    def createMyLogger(cls):
        cls.getMyLogger()

        strOutput = "MyLogger not initialized. Had to create logger using default params."
        cls.logWarn(strOutput)

    @classmethod
    def logDebug(cls, msg):
        """
        Log a DEBUG level msg
        """
        if cls.myLog is None:
            cls.createMyLogger()

        cls.myLog.debug(msg)

    @classmethod
    def logInfo(cls,msg):
        """
        Log an INFO level msg
        """
        if cls.myLog is None:
            cls.createMyLogger()

        strOutput = msg
        cls.myLog.info(strOutput)

    @classmethod
    def logWarn(cls,msg):
        """
        Log a WARNING level msg
        """
        if cls.myLog is None:
            cls.createMyLogger()

        strOutput = msg
        cls.myLog.warning(strOutput)

    @classmethod
    def logError(cls, msg):
        """
        Log an ERROR level msg
        """
        if cls.myLog is None:
            cls.createMyLogger()

        cls.myLog.error(msg)

    @classmethod
    def logException(cls, Ex):
        """
        Log an ERROR level msg and the exception Ex
        """
        if cls.myLog is None:
            cls.createMyLogger()

        cls.myLog.exception(Ex)

    # Logging decorator for enter and exit of methods
    # Decorator must be under the @classmethod decorator (bottom up processing) else error accessing __name__ attrib for class methods
    def log_decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            funcName = func.__qualname__ if func.__qualname__ else func.__name__
            args_repr = [repr(a) for a in args]                      
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  
            signature = ", ".join(args_repr + kwargs_repr)           

            #with TraceLog(funcName, signature):
            try:
                EnterMsg = "Entering {}({})".format(funcName,signature)
                MyLogger.logDebug(EnterMsg)
                startTime = perf_counter_ns()

                return func(*args,**kwargs)
            except Exception as Ex:
                strOutputError = "Unhandled exception occurred."
                print(strOutputError)
                # Log and Quit
                MyLogger.logException(Ex)
                #print(Ex)
                raise
            finally:
                endTime = perf_counter_ns()
                runTime = endTime - startTime
                ExitMsg = "Exiting {} in {} ns".format(funcName, runTime)

                MyLogger.logDebug(ExitMsg)
        return wrapper

    # DEPRECATED - used below within each method to log
    #MyLogger.TraceEnter(type(self).__qualname__ +"."+sys._getframe().f_code.co_name)
    #@classmethod
    #def TraceEnter(cls,msg):
    #    strOutput = "Entering " + msg
    #    cls.myLog.info(strOutput)

    # DEPRECATED - used below within each method to log
    #MyLogger.TraceExit(type(self).__qualname__ +"."+sys._getframe().f_code.co_name)
    #@classmethod
    #def TraceExit(cls,msg):
    #    strOutput = "Exiting " + msg
    #    cls.myLog.info(strOutput)

# Trace class to log enter and exit of methods
class TraceLog(object):
    def __init__(self, funcName, signature):
        self.funcName = funcName
        self.signature = signature

    def __enter__(self):
        EnterMsg = "Entering {}({})".format(funcName,signature)
        MyLogger.logDebug(EnterMsg)
        self.startTime = perf_counter_ns()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.endTime = perf_counter_ns()
        runTime = self.endTime - self.startTime
        ExitMsg = "Exiting " + self.funcName + " in " + str(runTime) + " ns"
        MyLogger.logDebug(ExitMsg)


