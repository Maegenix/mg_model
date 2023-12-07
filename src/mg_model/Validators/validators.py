import re
from typing import *
from mg_model.Exceptions import InvalidPassword, InvalidUsername


class ValidatorExpression:
    def __init__(self, expression: str | int, message: str, condition: str = None):
        self.exp = expression
        self.message = message
        self.condition = condition


class Validator:
    def __init__(
        self,
        exception: Exception,
        requirements: list[ValidatorExpression],
        operation: Callable = re.match,
    ):
        self._exception = exception
        self._requirements = requirements
        self._operation = operation

    def validate(self, value: str) -> bool:
        for req in self._requirements:
            if not self.__checkExpression(req.exp, value, req.condition):
                raise self._exception(req.message)
        return True

    def __checkExpression(self, expression: str | int, value: str, condition: str):
        return (
            eval(f"{len(value)} {condition} {expression}")
            if condition
            else self._operation(expression, value)
        )


class PasswordValidator(Validator):
    def __init__(self):
        super().__init__(
            InvalidPassword,
            [
                ValidatorExpression(8, "Password must be 8 charaters.", ">="),
                ValidatorExpression(
                    "[A-Z]", "Password must contain an upper-case letter."
                ),
                ValidatorExpression("[0-9]", "Password must contain a number."),
                ValidatorExpression(
                    "[@#$!]", "Password must contain a special character (@, #, $, !)."
                ),
            ],
            re.search,
        )


class UsernameValidator(Validator):
    def __init__(self):
        super().__init__(
            InvalidUsername,
            [
                ValidatorExpression(3, "Username must be atleast 3 charaters.", ">="),
                ValidatorExpression(12, "Username must be 12 charaters or less.", "<="),
                ValidatorExpression(
                    "^[A-Za-zÀ-ȕ0-9\-_\.]*$", "Invalid Username character."
                ),
            ],
        )


class EmailValidator(Validator):
    def __init__(self):
        super().__init__(
            InvalidUsername,
            [
                ValidatorExpression("^\S+@\S+\.\S+$", "Invalid email."),
            ],
        )


class ValidateNewUser:
    def __init__(self, email, password):
        EmailValidator().validate(email)
        PasswordValidator().validate(password)
