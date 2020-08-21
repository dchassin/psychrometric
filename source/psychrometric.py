"""
Psychrometric (temperature and humidity) calculations

All temperature and dewpoint values are in Celcius. Humidity values are in % (relative humidity). See https://en.wikipedia.org/wiki/Psychrometrics for details.

Source: http://bmcnoldy.rsmas.miami.edu/Humidity.html (August 2020)

References:

* Alduchov, O. A., and R. E. Eskridge, 1996: Improved Magnus' form approximation of saturation vapor pressure. J. Appl. Meteor., 35, 601–609. 

* August, E. F., 1828: Ueber die Berechnung der Expansivkraft des Wasserdunstes. Ann. Phys. Chem., 13, 122–137. 

* Magnus, G., 1844: Versuche über die Spannkräfte des Wasserdampfs. Ann. Phys. Chem., 61, 225–247.

Examples:
>>> import psychrometric as pm
>>> pm.Temperature(value=20,unit="C")
293.16
>>> pm.Temperature(20,"C").F()
68.0
>>> pm.Temperature(100,"C").F()
212.0
>>> pm.Temperature(100,"F").humidity(dewpoint=pm.Temperature(70,"F"))
38.19555954648607

"""

from math import *

class Temperature(float):

    """Temperature class that implements conversion between temperature units"""

    def __new__(cls,value,unit="K",noexception=False):

        """Define a temperature value with associated units

        Parameters:
          * value (float): temperature value
          * unit (str): temperature unit, i.e., 'K' (default),'C','F', or 'R'
        """
        if unit == "K":
            return float.__new__(cls,value)
        elif unit == "C":
            return float.__new__(cls,value+273.16)
        elif unit == "F":
            return float.__new__(cls,(value-32)*5/9+273.16)
        elif unit == "R":
            return float.__new__(cls,value*5/9)
        elif noexception:
            return None
        else:
            raise Exception(f"psychrometric.Temperature(value={value},unit='{unit}'): unit '{unit}' is not valid")

    def __add__(self,T):
        """Add temperatures"""
        return Temperature(float(self)+float(T),"K")

    def __sub__(self,T):
        """Subtract temperatures"""
        return Temperature(float(self)-float(T),"K")

    def __mul__(self,a):
        """Multiple temperature by a scalar"""
        return Temperature(float(self)*a,"K")

    def __truediv__(self,a):
        """Divide temperature by a scalar or temperature"""
        if type(a) == Temperature:
            return float(self)/float(a)
        else:
            return Temperature(float(self)/a,"K")

    def K(self):
        """Convert temperature value to Kelvin"""
        return float(self)

    def C(self):
        """Convert temperature value to Celcius"""
        return float(self)-273.16

    def F(self):
        """Convert temperature value to Fahrenheit

        Important Note: use Rankine scale for all add/subtract Fahrentheit operations.
        """
        return (float(self)-273.16)*9/5+32

    def R(self):
        """Convert temperature value to Rankine

        Important Note: use Rankine scale for all add/subtract Fahrentheit operations.
        """
        return float(self)*9/5

    def humidity(self,dewpoint):
        """Calculate the relative humidity for the given dewpoint
        Parameters:
          * (Temperature) dewpoint temperature
        Returns:
          (float) relative humidity in %
        """
        return humidity(self.C(),dewpoint.C())

    def dewpoint(self,humidity):
        """Calculate the dewpoint temperature given the relative humidity
        Parameters:
          * (float) relative humidity (%)
        Returns:
          * (Temperature) dewpoint temperature
        """
        return Temperature(dewpoint(self.C(),humidity),"C")

def temperature(RH,DP):
    """Calculate temperative given relative humidity and dewpoint temperature (all temperature in Celcius)"""
    return 243.04*(((17.625*DP)/(243.04+DP))-log(RH/100))/(17.625+log(RH/100)-((17.625*DP)/(243.04+DP)))

def humidity(T,DP):
    """Calculate relative humidity given temperative and dewpoint temperature (all temperature in Celcius)"""
    return 100*(exp((17.625*DP)/(243.04+DP))/exp((17.625*T)/(243.04+T)))

def dewpoint(T,RH):
    """Calculate dewpoint temperature given relative humidity and temperative (all temperature in Celcius)"""
    return 243.04*(log(RH/100)+((17.625*T)/(243.04+T)))/(17.625-log(RH/100)-((17.625*T)/(243.04+T)))

import unittest

class TestTemperature(unittest.TestCase):

    def test_Kelvin(self):
        self.assertEqual(Temperature(0).K(),0)
        self.assertEqual(Temperature(0,"K").K(),0)
        self.assertEqual(Temperature(290).K(),290)
        self.assertEqual(Temperature(290,"K")+100,390)
        self.assertEqual(Temperature(0,"K")+Temperature(20,"K"),20)
        self.assertEqual((Temperature(400,"K")-Temperature(100,"K")).K(),300)
        self.assertEqual((Temperature(293.16,"K")-Temperature(20,"K")).K(),273.16)
        self.assertEqual((Temperature(100,"K")*2).K(),200)
        self.assertEqual((Temperature(100,"K")*2).K(),Temperature(200,"K").K())
        self.assertEqual((Temperature(100,"K")/2),Temperature(50,"K"))
        self.assertEqual((Temperature(100,"K")/Temperature(50,"K")),2)

        self.assertEqual(Temperature(20,"C").C(),20)
        self.assertEqual(Temperature(10,"C").C(),10)
        self.assertEqual(Temperature(0,"C").K(),273.16)
        self.assertEqual(Temperature(100,"C").K(),373.16)
        self.assertEqual(Temperature(32,"F").K(),273.16)
        self.assertEqual(Temperature(212,"F").K(),373.16)
        self.assertEqual(Temperature(0,"J",True),None)
        self.assertLess(abs(Temperature(20,"C").humidity(Temperature(10,"C"))-52.54),0.01)
        self.assertLess(abs(Temperature(20,"C").dewpoint(52.54).C()-Temperature(10,"C").C()),0.01)

class TestPsychrometric(unittest.TestCase):

    def test_temperature(self):
        self.assertLess(abs(temperature(70.0,20.0)-25.89),0.01)

    def test_humidity(self):
        self.assertLess(abs(humidity(20.0,10.0)-52.54),0.01)

    def test_dewpoint(self):
        self.assertLess(abs(temperature(70.0,10.0)-15.45),0.01)

if __name__ == '__main__':
    unittest.main()
