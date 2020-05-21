import logging

class MyLogger(logging.getLoggerClass()):

    myLog = ""

    @classmethod
    def getMyLogger(cls, logFileName, logFileMode, logName, logLevel):
        # create logger
        cls.myLog = logging.getLogger(logName)
        cls.myLog.setLevel(logLevel)

        # create formatter and add it to the handlers
        myLogFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # create file handler for logger.
        myLogFH = logging.FileHandler(logFileName, logFileMode)
        myLogFH.setLevel(logLevel)
        myLogFH.setFormatter(myLogFormat)

        cls.myLog.addHandler(myLogFH)

    @classmethod
    def TraceEnter(cls,msg):
        strOutput = "Entering " + msg
        cls.myLog.info(strOutput)

    @classmethod
    def TraceExit(cls,msg):
        strOutput = "Exiting " + msg
        cls.myLog.info(strOutput)
