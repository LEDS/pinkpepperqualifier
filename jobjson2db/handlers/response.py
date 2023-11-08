class Response:
    # Environment Variables
    envVar_exception = "EXCEPTION_IMAGERESPONSE"
    # Exceptions Keys
    exception_initParSuccessedType = "WRONG_TYPE_PAR_INIT_SUCCESSED"
    exception_initParDataType = "WRONG_TYPE_PAR_INIT_DATA"
    exception_initParErrorMsgType = "WRONG_TYPE_PAR_INIT_ERROR_MSG"

    def __init__(self, *, successed: bool, data: NoneType | np.ndarray = None, error_msg: NoneType | str = None) -> NoneType:
        eh: EnvironmentHandler = EnvironmentHandler()
        self.exceptions_msg = eh.get_json(envVar = self.envVar_exception)

        if not isinstance(successed, bool):
            raise TypeError(self.exceptions_msg.get(self.exception_initParSuccessedType, ""))
        #if data is not None and not isinstance(data, np.ndarray):
        #    raise TypeError(self.exceptions_msg.get(self.exception_initParDataType, ""))
        if error_msg is not None and not isinstance(error_msg, str):
            raise TypeError(self.exceptions_msg.get(self.exception_initParErrorMsgType, ""))

        self.successed = successed
        self.data = data
        self.error_msg = error_msg

    def __str__(self):
        return f"ImageResponse(successed = {self.successed}, data = {self.data is not None}, error_msg = {self.error_msg is not None})"

    __repr__ = __str__