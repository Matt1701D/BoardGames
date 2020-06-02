import unittest, os
from MyLogger.MyLogger import MyLogger
from MyLogger.MyExceptions import *

class Test_MyLogger(unittest.TestCase):
    def test_CreateLogger(self):
        #Arrange
        logFileName = "TestLog.log"
        logFileMode = "w"
        logName = "TestLog"
        logLevel = "DEBUG"        

        #Act
        MyLogger.getMyLogger(logFileName=logFileName,logFileMode=logFileMode,logName=logName,logLevel=logLevel)
        myLoggerFile = MyLogger.myLog.handlers[0].baseFilename

        #Assert
        self.assertIsNotNone(MyLogger.myLog)
        assert os.path.exists(myLoggerFile)

    def test_CustomException(self):
        #Arrange
        logFileName = "TestLog.log"
        logFileMode = "w"
        logName = "TestLog"
        logLevel = "ERROR"   
        myExFound = False

        #Act
        MyLogger.getMyLogger(logFileName=logFileName,logFileMode=logFileMode,logName=logName,logLevel=logLevel)
        myLoggerFile = MyLogger.myLog.handlers[0].baseFilename

        try:
            raise InvalidParameterException("testParam","testValue","^[0-9]$")
        except InvalidParameterException as IPEx:
            MyLogger.logException(IPEx)

        #Assert
        with open(myLoggerFile) as file:
            for line in file:
                if "InvalidParameterException" in line:
                    myExFound = True
                    break

        self.assertTrue(myExFound)

if __name__ == '__main__':
    unittest.main()
