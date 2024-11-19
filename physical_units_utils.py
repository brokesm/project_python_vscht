"""
This module implements various functions for physical units conversion.
"""

import numbers


def convert_speed(value, actual_unit: str, target_unit: str):
    """
    Convert speed value from actual_unit to target_unit. Return converted value.
    :param value: numeric value to convert
    :param actual_unit: string actual physical unit (mph, kph)
    :param target_unit: string target physical unit (mph, kph)
    :return: converted value
    :raises ValueError: exception due to wrong value, actual_unit, target_unit value
    """
    # test acceptable inputs
    if isinstance(value, numbers.Number) and \
            all(x in ["mph", "kph"] for x in [actual_unit, target_unit]):
        # check units equality
        if actual_unit == target_unit:
            return value
        # dictionary for conversion, key is target unit
        conversion = {"kph": lambda x: x * 0.621371192,
                      "mph": lambda x: x * 1.60934
                      }
        return conversion[target_unit](value)
    raise ValueError("value must be numeric,"
                     " actual_unit and target_unit accept only mph or kph values")
