class ServerFailedRequestError(Exception):
    _MESSAGE = "Server failed request"

    def __init__(self, message: str = _MESSAGE):
        super().__init__(message)