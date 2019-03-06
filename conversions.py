#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert from one temperature unit to another temperature unit."""


class ConversionError(Exception): pass
class InvalidInputError(ConversionError): pass
class NotIntegerError(Exception): pass
class LowLimitError(Exception): pass



def convertCelciusToKelvin(celcius):
    """Convert Celcius temperature to Kelvin"""
    if int(celcius) != celcius:
        raise NotIntegerError('Input must be numeric value')

    if not celcius > -274:
        raise LowLimitError('Input is below absolute zero temperature')

    kelvin = celcius + 273

    return kelvin


def convertCelciusToFahrenheit(celcius):
    """Convert Celcius temperature to Fahrenheit"""
    if int(celcius) != celcius:
        raise NotIntegerError('Input must be integer value')

    if not celcius >= -273:
        raise LowLimitError('Input value must be higher than absolute zero temperature')

    fahrenheit = ((celcius * 9) / 5) + 32

    return fahrenheit


def convertKelvinToCelcius(kelvin):
    """Convert Kelvin to Celcius"""
    if int(kelvin) != kelvin:
        raise NotIntegerError('Input value must be an integer')

    if not kelvin > -1:
        raise LowLimitError('Input value must be higher than absolute zero temperature')

    celcius = kelvin - 273

    return celcius


def convertKelvinToFahrenheit(kelvin):
    """Convert Kelvin to Celcius."""
    if int(kelvin) != kelvin:
        raise NotIntegerError('Input value must be an integer')

    if not kelvin > 0:
        raise LowLimitError('Input value must be higher than absolute zero temperature')

    fahrenheit = (((kelvin - 273) * 9) / 5) + 32

    return fahrenheit


def convertFahrenheitToKelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    if int(fahrenheit) != fahrenheit:
        raise NotIntegerError('Input value must be an integer')

    if not fahrenheit > -461:
        raise LowLimitError('Input value must be higher than absolute zero temperature')

    kelvin = ((fahrenheit - 32) * 5) / 9 + 273

    return kelvin


def convertFahrenheitToCelcius(fahrenheit):
    """Convert Fahrenheit to Celcius"""
    if int(fahrenheit) != fahrenheit:
        raise NotIntegerError('Input value must be an integer')

    if not fahrenheit > -461:
        raise LowLimitError('Input value must be higher than absolute zero temperature')

    celcius = ((fahrenheit - 32) * 5) / 9

    return celcius
