import unittest, os
from MyLogger.MyLogger import MyLogger
from MyLogger.MyExceptions import *

class Test_MyLogger(unittest.TestCase):
    def test_CreateFileLogger(self):
        #Arrange
        logFileName = "TestLog.log"
        logFileMode = "w"
        logName = "TestLogFile"
        logLevel = "DEBUG"        

        #Act
        MyLogger.addFileLogger(logFileName=logFileName,logFileMode=logFileMode,logName=logName,logLevel=logLevel)
        myLoggerFile = MyLogger.myLog["File"].handlers[0].baseFilename

        #Assert
        self.assertIsNotNone(MyLogger.myLog["File"])
        assert os.path.exists(myLoggerFile)

    def test_CreateDBLogger(self):
        #Arrange
        logName = "TestLogDB"
        logTableName = "GameCenter"
        logLevel="DEBUG"
        logConnString = ""
        logDBName = "Log"    

        #Act
        MyLogger.addDBLogger(logName, logConnString, logDBName, logTableName, logLevel)

        #Assert
        self.assertIsNotNone(MyLogger.myLog["DB"])

    def test_LogToDB(self):
        #Arrange
        logName = "TestLogDB"
        logTableName = "GameCenter"
        logLevel="DEBUG"
        logConnString = ""
        logDBName = "Log"    

        #Act
        MyLogger.addDBLogger(logName, logConnString, logDBName, logTableName, logLevel)
        actResult = MyLogger.logDebug(["DB"],"test")

        #Assert
        self.assertTrue(actResult)

    def test_CustomException(self):
        #Arrange
        logFileName = "TestLog.log"
        logFileMode = "w"
        logName = "TestLogFile"
        logLevel = "ERROR"   
        myExFound = False

        #Act
        MyLogger.addFileLogger(logFileName=logFileName,logFileMode=logFileMode,logName=logName,logLevel=logLevel)
        myLoggerFile = MyLogger.myLog["File"].handlers[0].baseFilename

        try:
            raise InvalidParameterException("testParam","testValue","^[0-9]$")
        except InvalidParameterException as IPEx:
            MyLogger.logException(["File"],IPEx)

        #Assert
        with open(myLoggerFile) as file:
            for line in file:
                if "InvalidParameterException" in line:
                    myExFound = True
                    break

        self.assertTrue(myExFound)

if __name__ == '__main__':
    unittest.main()
