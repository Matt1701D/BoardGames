import logging, functools
from time import perf_counter_ns
from MyLogger.MyExceptions import *

class MyLogger(logging.getLoggerClass()):

    logFileName = "GameCenter.log"
    logFileMode = "w"
    logName = "GameCenter"
    logLevel = "DEBUG"
    myLog = None

    # CONSTRUCTOR

    @classmethod
    def getMyLogger(cls, **kwargs):
        """
        Create new logger. Optional params by keyword:
        1) logFileName: name of log file
        2) logFileMode: file write mode, default is 'w' to truncate existing log
        3) logName: name for this logger
        4) logLevel: level to filter log, order is DEBUG,INFO,WARNING,ERROR
        """
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

    # LOG METHODS

    @classmethod
    def logDebug(cls, msg):
        """
        Log a DEBUG level msg
        """
        if cls.myLog is None:
            cls.__createMyLogger()

        cls.myLog.debug(msg)

    @classmethod
    def logInfo(cls,msg):
        """
        Log an INFO level msg
        """
        if cls.myLog is None:
            cls.__createMyLogger()

        strOutput = msg
        cls.myLog.info(strOutput)

    @classmethod
    def logWarn(cls,msg):
        """
        Log a WARNING level msg
        """
        if cls.myLog is None:
            cls.__createMyLogger()

        strOutput = msg
        cls.myLog.warning(strOutput)

    @classmethod
    def logError(cls, msg):
        """
        Log an ERROR level msg
        """
        if cls.myLog is None:
            cls.__createMyLogger()

        cls.myLog.error(msg)

    @classmethod
    def logException(cls, Ex):
        """
        Log an ERROR level msg and the exception Ex
        """
        if cls.myLog is None:
            cls.__createMyLogger()

        cls.myLog.exception(Ex)

    # DECORATOR

    def log_decorator(func):
        """
        Logging decorator for enter and exit of methods, catches all unknown Exceptions. Any explicit exceptions should be handled by client
        Decorator must be under the @classmethod decorator (bottom up processing) else error accessing __name__ attrib for class methods
        """
        @functools.wraps(func) # preserves calling func info, not sure if needed
        def wrapper(*args,**kwargs):
            funcName = func.__qualname__ if func.__qualname__ else func.__name__
            args_repr = [repr(a) for a in args]                      
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  #!r forces to use print friendlier __repr__ instead of __str__
            signature = ", ".join(args_repr + kwargs_repr)           

            with TraceLog(funcName, signature):
                try:
                    return func(*args,**kwargs)
                # Handle all unknown exceptions here
                except Exception as Ex:
                    strOutputError = "Unhandled exception occurred."
                    print(strOutputError)

                    # Log and Quit
                    MyLogger.logException(Ex)
                    raise

        return wrapper

    # PRIVATE METHODS

    # Create a default logger if one has not been created
    @classmethod
    def __createMyLogger(cls):
        cls.getMyLogger()

        strOutput = "MyLogger not initialized. Had to create logger using default params."
        cls.logWarn(strOutput)


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

# Trace class context manager to log enter and exit of methods
class TraceLog(object):
    def __init__(self, funcName, signature):
        self.funcName = funcName
        self.signature = signature

    def __enter__(self):
        EnterMsg = f"Entering {self.funcName}({self.signature})"
        MyLogger.logDebug(EnterMsg)
        self.startTime = perf_counter_ns()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.endTime = perf_counter_ns()
        runTime = self.endTime - self.startTime
        ExitMsg = F"Exiting {self.funcName} in {str(runTime)} ns"
        MyLogger.logDebug(ExitMsg)


