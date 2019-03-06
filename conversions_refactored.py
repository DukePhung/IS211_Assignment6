#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert from one temperature unit to another temperature unit."""

import conversions

class ConversionError(Exception): pass
class ConversionNotPossible(ConversionError): pass

def convert(fromUnit, toUnit, value):
    """Convert fromUnit value to toUnit."""

    if fromUnit == 'Fahrenheit':
        if toUnit == 'Celcius':
            return float(conversions.convertFahrenheitToCelcius(value))
        elif toUnit == 'Kelvin':
            return float(conversions.convertFahrenheitToKelvin(value))
        else:
            raise ConversionError('{} cannot be converted to {}'.format(fromUnit, toUnit))

    elif fromUnit == 'Celcius':
        if toUnit == 'Fahrenheit':
            return float(conversions.convertCelciusToFahrenheit(value))
        elif toUnit == 'Kelvin':
            return float(conversions.convertCelciusToKelvin(value))
        else:
            raise ConversionError('{} cannot be converted to {}'.format(fromUnit, toUnit))

    elif fromUnit == 'Kelvin':
        if toUnit == 'Fahrenheit':
            return float(conversions.convertKelvinToFahrenheit(value))
        elif toUnit == 'Celcius':
            return float(conversions.convertKelvinToCelcius(value))

    else:
        raise ConversionNotPossible('Cannot perform conversions')

if __name__ == '__main__':
    print(convert('Fahrenheit', 'Kelvin', 212))
    print(convert('Celcius', 'Kelvin', 212))
    print(convert('Celcius', 'Miles', 212))

