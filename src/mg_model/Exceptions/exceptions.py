class UserNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidPassword(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidUsername(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidEmail(Exception):
    def __init__(self, message):
        super().__init__(message)


class ExistingUser(Exception):
    def __init__(self, message):
        super().__init__(message)
