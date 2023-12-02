class ServerUnavailableError(Exception):
    _MESSAGE = "Server is unavailable"

    def __init__(self, message: str = _MESSAGE):
        super().__init__(message)
