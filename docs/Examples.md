To use temperature and psychrometric module you must import the library first:

~~~
>>> from psychrometric import *
~~~

# Temperatures

All temperatures are represented internally in Kelvin.

~~~
>>> Temperature(0)
psychrometric.Temperature(value=0.0,unit='K')
>>> Temperature(0,"C")
psychrometric.Temperature(value=273.16,unit='K')
>>> Temperature(32,"F")
psychrometric.Temperature(value=273.16,unit='K')
>>> Temperature(491.688,"R")
psychrometric.Temperature(value=273.16,unit='K')
~~~

Temperature objects can be presented as evaluatable constructors, e.g.,

~~~
>>> repr(Temperature(100,"C"))
"psychrometric.Temperature(value=373.16,unit='K')"
~~~

or strings, e.g.,

~~~
>>> str(Temperature(100,"C"))
'373.16 degK'
~~~

Basic temperature conversion is supported

~~~
>>> Temperature(0,"C").K()
273.16
>>> Temperature(0,"C").F()
32.0
>>> Temperature(300,"K").F()
80.31199999999995
~~~

Temperature addition and subtraction can be performed using the underlying `float` or `Temperature` classes:

~~~
>>> Temperature(300,"K") + Temperature(10,"K")
psychrometric.Temperature(value=310.0,unit='K')
>>> Temperature(300,"K") - Temperature(10,"K")
psychrometric.Temperature(value=290.0,unit='K')
~~~

Note that when adding and subtracting temperature, using Celcius `C` or Fahrenheit `F` operands will yield unexpected results. Be sure to use the absolute scales, i.e., Kelvin `K` or Rankine `R`, e.g.,

~~~
>>> ( Temperature(32,"F") + Temperature(9,'R') ).C()
5.0
~~~

Temperature multiplication can only be performed with an underlying `float` operand, e.g.,

~~~
>>> Temperature(300,"K") * 1.1
psychrometric.Temperature(value=330.0,unit='K')
>>> Temperature(300,"K") / 1.5
psychrometric.Temperature(value=200.0,unit='K')
~~~

Temperature division can be performend with either an underlying `float` or `Temperature` operand. However, the type of the result will differ depending on whether the result is a Temperature or a ratio, e.g.,

~~~
>>> Temperature(32,"F") / 2
psychrometric.Temperature(value=136.58,unit='K')
>>> Temperature(100,"F") / Temperature(32,"F")
1.1382990839719496
~~~

# Psychrometrics

The temperature/humidity calculation can be used in two ways.  The raw calculations are available for `float` objects provided the numbers are always presented in Celcius, e.g.,

~~~
>>> humidity(temperature=70,dewpoint=50)
39.300969741521484
>>> temperature(dewpoint=50,humidity=40)
69.59719734621933
>>> dewpoint(temperature=70,humidity=40)
50.35385860734516
~~~

In addition, the `Temperature` class support the same conversions, e.g.,

~~~
>>> Temperature(68,"F").humidity(dewpoint=Temperature(50,"F"))
52.54132558106588
>>> Temperature(68,"F").dewpoint(humidity=50).F()
48.66999193496164
~~~

You can create a `Temperature` from a humidity and dewpoint using the `Temperature` constructor, e.g.,

~~~
>>> Temperature(dewpoint=Temperature(70,"F"),humidity=70).F()
80.69305750960189
~~~
