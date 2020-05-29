class InvalidParameterException(BaseException):
    def __init__(self, paramName, paramValue, expRegEx):
        super().__init__()
        self.paramName = paramName
        self.paramValue = paramValue
        self.expRegEx = expRegEx       

    def __str__(self):
        msg = "Invalid value \'{}\' for parameter {}. Expected RegEx pattern {}".format(self.paramValue, self.paramName, self.expRegEx)
        return msg
