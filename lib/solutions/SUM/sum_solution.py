# noinspection PyShadowingBuiltins,PyUnusedLocal
import logging

class OutOfRangeException(Exception):
    pass

class NegativeValuesException(Exception):
    pass

class InvalidTypeProvidedException(Exception):
    pass

def validate_inputs(x, y):
    if not isinstance(x, int) and not isinstance(y, int):
        raise InvalidTypeProvidedException('Invalid input detected')

    if x < 0 or y < 0:
        raise NegativeValuesException('Negative values are not allowed')

    if 0 <= x <= 100 and 0 <= y <= 100:
        return True
    
    raise OutOfRangeException('You can only enter numbers between 0 and 100')


def compute(x, y):
    try:
        validate_inputs(x, y)

        return x + y
    except (OutOfRangeException, NegativeValuesException):
        logging.error("Invalid input, does not confirm to postive and in-range values")
        raise
    except InvalidTypeProvidedException:
        logging.error("Only Integers can be passed into sum function")
        raise






