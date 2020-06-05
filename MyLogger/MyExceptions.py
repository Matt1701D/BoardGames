class InvalidParameterException(BaseException):
    def __init__(self, paramName, paramValue, expRegEx):
        super().__init__()
        self.paramName = paramName
        self.paramValue = paramValue
        self.expRegEx = expRegEx       

    def __str__(self):
        msg = f"Invalid value \'{self.paramValue}\' for parameter {self.paramName}. Expected RegEx pattern {self.expRegEx}"
        return msg

class LoggingError(BaseException):
    def __init__(self, record):
        super().__init__() 
        self.record = record

    def __str__(self):
        msg = f"Error occcurred in logger: {record}"
        return msg
