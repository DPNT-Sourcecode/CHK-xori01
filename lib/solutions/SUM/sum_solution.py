# noinspection PyShadowingBuiltins,PyUnusedLocal

class OutOfRangeException(Exception):
    pass

class NegativeValuesException(Exception):
    pass

class InvalidTypeProvidedException(Exception):
    pass

def validate_inputs(x, y):
    if not isinstance(x, int) and not isinstance(y, int):
        raise InvalidTypeProvidedException('Invalid input detected')

    if x < 0 and y < 0:
        raise NegativeValuesException('Negative values are not allowed')

    if 0 <= x <= 100 and 0 <= y <= 100:
        return True
    
    raise OutOfRangeException('You can only enter numbers between 0 and 100')


def compute(x, y):
    try:
        validate_inputs




