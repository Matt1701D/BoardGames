import logging, functools, pymongo
from time import perf_counter_ns
from MyLogger.MyExceptions import *

class MyLogger(logging.getLoggerClass()):

    myLog = {}
    logging.raiseExceptions = True

    # CONSTRUCTORS

    # TODO
    # Make sure logName is different for all loggers unless want to log to both?

    @classmethod
    def addFileLogger(cls, logFileName, logName, logFileMode="w", logLevel="ERROR"):
        """
        Create new File logger. Optional params by keyword:
        1) logFileName: name of log file
        2) logFileMode: file write mode, default is 'w' to truncate existing log
        3) logName: name for this logger
        4) logLevel: level to filter log, order is DEBUG,INFO,WARNING,ERROR (default)
        """

        if cls.myLog.get("File",None) is None:
            # create logger
            myFileLog = logging.getLogger(logName)
            myFileLog.setLevel(logLevel)           

            # create formatter
            myLogFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
            # create file handler for logger.
            myLogFH = MyFileHandler(logFileName, logFileMode)
            myLogFH.setLevel(logLevel)
            myLogFH.setFormatter(myLogFormat)

            # add the file handler to the logger
            myFileLog.addHandler(myLogFH)

            # add file logger to dict of loggers to use
            cls.myLog["File"] = myFileLog

    @classmethod
    def addDBLogger(cls, logName, logConnString, logDBName, logTableName, logLevel="ERROR"):
        """
        Create new Database logger. Optional params by keyword:
        1) logName: name for this logger
        2) logConnString: connection string to database
        3) logDBName: name of the database to log to 
        4) logTableName: name of the table to log to
        5) logLevel: level to filter log, order is DEBUG,INFO,WARNING,ERROR (default)
        """

        if cls.myLog.get("DB",None) is None:
            # create logger
            myDBLog = logging.getLogger(logName)
            myDBLog.setLevel(logLevel)

            # create formatter
            myLogFormat = logging.Formatter("{'TimeStamp':'%(asctime)s', 'LogName':'%(name)s', 'LogLevel':'%(levelname)s', 'Message':'%(message)s'}")
        
            # create file handler for logger.
            myLogDH = MongoDatabaseHandler(logConnString, logDBName, logTableName)
            myLogDH.setLevel(logLevel)
            myLogDH.setFormatter(myLogFormat)
            myLogDH.addFilter(FilterNoQuotes())

            # add the db handler to the logger
            myDBLog.addHandler(myLogDH)

            # add file logger to dict of loggers to use
            cls.myLog["DB"] = myDBLog

    # LOG METHODS

    @classmethod
    def logDebug(cls, loggers, msg):
        """
        Log a DEBUG level msg
        """
        availLoggers = cls.__checkForLogger(loggers)

        try:
            for logger in availLoggers:
                cls.myLog[logger].debug(msg)
            return True
        except:
            return False

    @classmethod
    def logInfo(cls, loggers, msg):
        """
        Log an INFO level msg
        """
        availLoggers = cls.__checkForLogger(loggers)

        strOutput = msg
        try:
            for logger in availLoggers:
                cls.myLog[logger].info(msg)
            return True
        except:
            return False

    @classmethod
    def logWarn(cls, loggers, msg):
        """
        Log a WARNING level msg
        """
        availLoggers = cls.__checkForLogger(loggers)

        strOutput = msg
        try:
            for logger in availLoggers:
                cls.myLog[logger].warning(msg)
            return True
        except:
            return False

    @classmethod
    def logError(cls, loggers, msg):
        """
        Log an ERROR level msg
        """
        availLoggers = cls.__checkForLogger(loggers)

        try:
            for logger in availLoggers:
                cls.myLog[logger].error(msg)
            return True
        except:
            return False

    @classmethod
    def logException(cls, loggers, Ex):
        """
        Log an ERROR level msg and the exception Ex
        """
        availLoggers = cls.__checkForLogger(loggers)

        try:
            for logger in availLoggers:
                cls.myLog[logger].exception(Ex)
            return True
        except:
            return False

    # DECORATOR

    def log(loggers):
        """
        Logging decorator for enter and exit of methods, catches all unknown Exceptions. Any explicit exceptions should be handled by client
        Decorator must be under the @classmethod decorator (bottom up processing) else error accessing __name__ attrib for class methods
        """
        def log_decorator(func):
            @functools.wraps(func) # preserves calling func info, not sure if needed
            def wrapper(*args,**kwargs):
                funcName = func.__qualname__ if func.__qualname__ else func.__name__
                args_repr = [repr(a) for a in args]                      
                kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  #!r forces to use print friendlier __repr__ instead of __str__
                signature = ", ".join(args_repr + kwargs_repr)           

                # TODO 
                # DONT PRINT MyLogger stack trace, see Handler.handleError()

                with TraceLog(loggers, funcName, signature):
                    try:
                        return func(*args,**kwargs)
                    # Handle all unknown exceptions here
                    except Exception as Ex:
                        strOutputError = "Unhandled exception occurred."
                        print(strOutputError)

                        # Log and Quit
                        MyLogger.logException(["DB"], Ex)
                        raise
            return wrapper
        return log_decorator

    # PRIVATE METHODS

    @classmethod
    def __checkForLogger(cls, loggers):
        availLoggers = []
        for logger in loggers:
            if logger in cls.myLog:
                availLoggers.append(logger)

        if len(availLoggers) == 0:
            cls.__defaultFileLogger()
            availLoggers.append("File")

        return availLoggers

    # Create a default logger if one has not been created
    @classmethod
    def __defaultFileLogger(cls):
        logFileName = "GameCenter.log"
        logName = "GameCenterLogFile"

        cls.addFileLogger(logFileName, logName)

        strOutput = "MyLogger not initialized. Had to create file logger using default params."
        cls.logWarn(["File"],strOutput)


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
    def __init__(self, loggers, funcName, signature):
        self.loggers = loggers
        self.funcName = funcName
        self.signature = signature

    def __enter__(self):
        EnterMsg = f"Entering {self.funcName}({self.signature})"
        MyLogger.logDebug(self.loggers, EnterMsg)
        self.startTime = perf_counter_ns()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.endTime = perf_counter_ns()
        runTime = self.endTime - self.startTime
        ExitMsg = F"Exiting {self.funcName} in {str(runTime)} ns"
        MyLogger.logDebug(self.loggers, ExitMsg)
        
# CUSTOM HANDLERS

# TODO
# Why cant call super().__init__()?

class MyBaseHandler(logging.Handler):
    def __init__(self):
        super(logging.Handler,self).__init__()

    def handleError(self, record):
        if logging.raiseExceptions:
            raise LoggingError(record)

class MyFileHandler(MyBaseHandler, logging.FileHandler):
    def __init__(self, logFileName, logFileMode):
        logging.FileHandler.__init__(self, logFileName, logFileMode)

class MongoDatabaseHandler(MyBaseHandler):
    myConn = None

    def __init__(self, connString, dbName, tbName, id=None):
        """
        Database handler for Logger. Specifiy connection to use, else MongoDB default connection string used
        """
        super(MyBaseHandler,self).__init__()
        self.connString = connString
        self.dbName = dbName
        self.tbName = tbName
        self.id = id

    def _open(self):
        self.myConn = pymongo.MongoClient()
        self.myDB = self.myConn[self.dbName]
        self.myTB = self.myDB[self.tbName]

    def format(self, record):
        rec = super(MyBaseHandler, self).format(record)
        return eval(rec)

    def emit(self, record):
        try:
            if self.myConn is None:
                self._open()

            rec = self.format(record)
            ins = self.myTB.insert_one(rec)
        except Exception:
            self.handleError(record)

    def close(self):
        self.myConn.close()

    def __repr__(self):
        level = getLevelName(self.level)
        conn = self.myConn[0] if self.myConn[0] is not None else self.connString
        return '<%s %s (%s)>' % (self.__class__.__name__, conn, level)

# CUSTOM FILTERS

class FilterNoQuotes(logging.Filter):

    def filter(self, record):
        record.msg = str(record.msg).replace("'", "HELLO")
        return record