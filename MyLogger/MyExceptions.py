class InvalidParameterException(BaseException):
    def __init__(self, paramName, paramValue, expRegEx):
        super().__init__()
        self.paramName = paramName
        self.paramValue = paramValue
        self.expRegEx = expRegEx       

    def __str__(self):
        msg = f"Invalid value \'{self.paramValue}\' for parameter {self.paramName}. Expected RegEx pattern {self.expRegEx}"
        return msg
