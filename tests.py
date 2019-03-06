#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert from one temperature unit to another temperature unit."""

import conversions
import unittest


class KnownValues(unittest.TestCase):

# knownValues tuple values in Celcius, Fahrenheit, Kelvin order

    knownValues = ((0, 32, 273), (10, 50, 283), (20, 68, 293), (30, 86, 303), (40, 104, 313),
                   (50, 122, 323), (80, 176, 353), (90, 194, 363), (100, 212, 373))

    def testConvertCelciusToKelvin(self):
        """convertCelciusToKelvin should give known result with known input"""
        for celcius, _, kelvin in self.knownValues:
            result = conversions.convertCelciusToKelvin(celcius)
            self.assertEqual(kelvin, result)

    def testconvertCelciusToFahrenheit(self):
        """convertCelciusToFahrenheit should give known result with known input"""
        for celcius, fahrenheit, _ in self.knownValues:
            result = conversions.convertCelciusToFahrenheit(celcius)
            self.assertEqual(fahrenheit, result)

    def testConvertKelvinToCelcius(self):
        """convertKelvinToCelcius should give known result with known input"""
        for celcius, _, kelvin in self.knownValues:
            result = conversions.convertKelvinToCelcius(kelvin)
            self.assertEqual(celcius, result)

    def testConvertKelvinToFahrenheit(self):
        """convertKelvinToFahrenheit should give known result with known input"""
        for _, fahrenheit, kelvin in self.knownValues:
            result = conversions.convertKelvinToFahrenheit(kelvin)
            self.assertEqual(fahrenheit, result)

    def testConvertFahrenheitToCelcius(self):
        """convertFahrenheitToCelcius should give known result with known input"""
        for celcius, fahrenheit, _ in self.knownValues:
            result = conversions.convertFahrenheitToCelcius(fahrenheit)
            self.assertEqual(celcius, result)

    def testConvertFahrenheitToKelvin(self):
        """convertFahrenheitToKelvin should give known result with known input"""
        for _, fahrenheit, kelvin in self.knownValues:
            result = conversions.convertFahrenheitToKelvin(fahrenheit)
            self.assertEqual(kelvin, result)

class BadInput(unittest.TestCase):

# Letters after testNonInteger denotes temperature measure

    def testNonIntegerCF(self):
        """convertCelciusToFahrenheit should fail with non-float input"""
        self.assertRaises(conversions.NotIntegerError, conversions.convertCelciusToFahrenheit, .9)

    def testNonIntegerCK(self):
        """convertCelciusToKelvin should fail with non-integer input"""
        self.assertRaises(conversions.NotIntegerError, conversions.convertCelciusToKelvin, .5)

    def testNonIntegerKC(self):
        """convertKelvinToCelcius should fail with non-integer input"""
        self.assertRaises(conversions.NotIntegerError, conversions.convertKelvinToCelcius, .2)

    def testNonIntegerKF(self):
        """convertKelvinToFahrenheit should fail with non-integer input"""
        self.assertRaises(conversions.NotIntegerError, conversions.convertKelvinToFahrenheit, .2)

    def testNonIntegerFC(self):
        """convertFahrenheitToCelcius should fail with non-integer input"""
        self.assertRaises(conversions.NotIntegerError, conversions.convertFahrenheitToCelcius, .8)

    def testNonIntegerFK(self):
        """convertFahrenheitToKelvin should fail with non-integer input"""
        self.assertRaises(conversions.NotIntegerError, conversions.convertFahrenheitToKelvin, .9)


class LowLimitExceeded(unittest.TestCase):

# Letters after testNonInteger denotes temperature measure

    def testLowLimitCK(self):
        """convertCelciusToKelvin should fail when input is below absolute zero."""
        self.assertRaises(conversions.LowLimitError, conversions.convertCelciusToKelvin, -274)

    def testLowLimitCF(self):
        """convertCelciusToFahrenheit should fail when input is below absolute zero."""
        self.assertRaises(conversions.LowLimitError, conversions.convertCelciusToFahrenheit, -274)

    def testLowLimitKC(self):
        """convertKelvinToCelcius should fail when input is below absolute zero."""
        self.assertRaises(conversions.LowLimitError, conversions.convertKelvinToCelcius, -1)

    def testLowLimitKF(self):
        """convertKelvinToFahrenheit should fail when input is below absolute zero."""
        self.assertRaises(conversions.LowLimitError, conversions.convertKelvinToFahrenheit, -1)

    def testLowLimitFC(self):
        """convertFahrenheitToCelcius should fail when input is below absolute zero."""
        self.assertRaises(conversions.LowLimitError, conversions.convertFahrenheitToCelcius, -461)

    def testLowLimitFK(self):
        """convertFahrenheitToKelvin should fail when input is below absolute zero."""
        self.assertRaises(conversions.LowLimitError, conversions.convertFahrenheitToKelvin, -461)


class SanityCheck(unittest.TestCase):

    def testSanityCelciusAndKelvin(self):
        """convertKelvinToCelcius(convertCelciusToKelvin(n))==n for all n"""
        for integer in range(1, 4000):
            numeral = conversions.convertCelciusToKelvin(integer)
            result = conversions.convertKelvinToCelcius(numeral)
            self.assertEqual(integer, result)


if __name__ == "__main__":
    unittest.main()
