Help on module psychrometric:

NAME
    psychrometric - Psychrometric (temperature and humidity) calculations

DESCRIPTION
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

CLASSES
    builtins.float(builtins.object)
        Temperature
    unittest.case.TestCase(builtins.object)
        TestPsychrometric
        TestTemperature
    
    class Temperature(builtins.float)
     |  Temperature(value, unit='K', noexception=False)
     |  
     |  Temperature class that implements conversion between temperature units
     |  
     |  Method resolution order:
     |      Temperature
     |      builtins.float
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  C(self)
     |      Convert temperature value to Celcius
     |  
     |  F(self)
     |      Convert temperature value to Fahrenheit
     |      
     |      Important Note: use Rankine scale for all add/subtract Fahrentheit operations.
     |  
     |  K(self)
     |      Convert temperature value to Kelvin
     |  
     |  R(self)
     |      Convert temperature value to Rankine
     |      
     |      Important Note: use Rankine scale for all add/subtract Fahrentheit operations.
     |  
     |  __add__(self, T)
     |      Add temperatures
     |  
     |  __mul__(self, a)
     |      Multiple temperature by a scalar
     |  
     |  __sub__(self, T)
     |      Subtract temperatures
     |  
     |  __truediv__(self, a)
     |      Divide temperature by a scalar or temperature
     |  
     |  dewpoint(self, humidity)
     |      Calculate the dewpoint temperature given the relative humidity
     |      Parameters:
     |        * (float) relative humidity (%)
     |      Returns:
     |        * (Temperature) dewpoint temperature
     |  
     |  humidity(self, dewpoint)
     |      Calculate the relative humidity for the given dewpoint
     |      Parameters:
     |        * (Temperature) dewpoint temperature
     |      Returns:
     |        (float) relative humidity in %
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(cls, value, unit='K', noexception=False)
     |      Define a temperature value with associated units
     |      
     |      Parameters:
     |        * value (float): temperature value
     |        * unit (str): temperature unit, i.e., 'K' (default),'C','F', or 'R'
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.float:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __float__(self, /)
     |      float(self)
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __format__(self, format_spec, /)
     |      Formats the float according to format_spec.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getnewargs__(self, /)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __int__(self, /)
     |      int(self)
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __round__(self, ndigits=None, /)
     |      Return the Integral closest to x, rounding half toward even.
     |      
     |      When an argument is passed, work like built-in round(x, ndigits).
     |  
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __trunc__(self, /)
     |      Return the Integral closest to x between 0 and x.
     |  
     |  as_integer_ratio(self, /)
     |      Return integer ratio.
     |      
     |      Return a pair of integers, whose ratio is exactly equal to the original float
     |      and with a positive denominator.
     |      
     |      Raise OverflowError on infinities and a ValueError on NaNs.
     |      
     |      >>> (10.0).as_integer_ratio()
     |      (10, 1)
     |      >>> (0.0).as_integer_ratio()
     |      (0, 1)
     |      >>> (-.25).as_integer_ratio()
     |      (-1, 4)
     |  
     |  conjugate(self, /)
     |      Return self, the complex conjugate of any float.
     |  
     |  hex(self, /)
     |      Return a hexadecimal representation of a floating-point number.
     |      
     |      >>> (-0.1).hex()
     |      '-0x1.999999999999ap-4'
     |      >>> 3.14159.hex()
     |      '0x1.921f9f01b866ep+1'
     |  
     |  is_integer(self, /)
     |      Return True if the float is an integer.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from builtins.float:
     |  
     |  __getformat__(typestr, /) from builtins.type
     |      You probably don't want to use this function.
     |      
     |        typestr
     |          Must be 'double' or 'float'.
     |      
     |      It exists mainly to be used in Python's test suite.
     |      
     |      This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
     |      little-endian' best describes the format of floating point numbers used by the
     |      C type named by typestr.
     |  
     |  __set_format__(typestr, fmt, /) from builtins.type
     |      You probably don't want to use this function.
     |      
     |        typestr
     |          Must be 'double' or 'float'.
     |        fmt
     |          Must be one of 'unknown', 'IEEE, big-endian' or 'IEEE, little-endian',
     |          and in addition can only be one of the latter two if it appears to
     |          match the underlying C reality.
     |      
     |      It exists mainly to be used in Python's test suite.
     |      
     |      Override the automatic determination of C-level floating point type.
     |      This affects how floats are converted to and from binary strings.
     |  
     |  fromhex(string, /) from builtins.type
     |      Create a floating-point number from a hexadecimal string.
     |      
     |      >>> float.fromhex('0x1.ffffp10')
     |      2047.984375
     |      >>> float.fromhex('-0x1p-1074')
     |      -5e-324
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.float:
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  real
     |      the real part of a complex number
    
    class TestPsychrometric(unittest.case.TestCase)
     |  TestPsychrometric(methodName='runTest')
     |  
     |  A class whose instances are single test cases.
     |  
     |  By default, the test code itself should be placed in a method named
     |  'runTest'.
     |  
     |  If the fixture may be used for many test cases, create as
     |  many test methods as are needed. When instantiating such a TestCase
     |  subclass, specify in the constructor arguments the name of the test method
     |  that the instance is to execute.
     |  
     |  Test authors should subclass TestCase for their own tests. Construction
     |  and deconstruction of the test's environment ('fixture') can be
     |  implemented by overriding the 'setUp' and 'tearDown' methods respectively.
     |  
     |  If it is necessary to override the __init__ method, the base class
     |  __init__ method must always be called. It is important that subclasses
     |  should not change the signature of their __init__ method, since instances
     |  of the classes are instantiated automatically by parts of the framework
     |  in order to be run.
     |  
     |  When subclassing TestCase, you can set these attributes:
     |  * failureException: determines which exception will be raised when
     |      the instance's assertion methods fail; test methods raising this
     |      exception will be deemed to have 'failed' rather than 'errored'.
     |  * longMessage: determines whether long messages (including repr of
     |      objects used in assert methods) will be printed on failure in *addition*
     |      to any explicit message passed.
     |  * maxDiff: sets the maximum length of a diff in failure messages
     |      by assert methods using difflib. It is looked up as an instance
     |      attribute so can be configured by individual tests if required.
     |  
     |  Method resolution order:
     |      TestPsychrometric
     |      unittest.case.TestCase
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  test_dewpoint(self)
     |  
     |  test_humidity(self)
     |  
     |  test_temperature(self)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from unittest.case.TestCase:
     |  
     |  __call__(self, *args, **kwds)
     |      Call self as a function.
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  __hash__(self)
     |      Return hash(self).
     |  
     |  __init__(self, methodName='runTest')
     |      Create an instance of the class that will use the named test
     |      method when executed. Raises a ValueError if the instance does
     |      not have a method with the specified name.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  addCleanup(*args, **kwargs)
     |      Add a function, with arguments, to be called when the test is
     |      completed. Functions added are called on a LIFO basis and are
     |      called after tearDown on test failure or success.
     |      
     |      Cleanup items are called even if setUp fails (unlike tearDown).
     |  
     |  addTypeEqualityFunc(self, typeobj, function)
     |      Add a type specific assertEqual style function to compare a type.
     |      
     |      This method is for use by TestCase subclasses that need to register
     |      their own type equality functions to provide nicer error messages.
     |      
     |      Args:
     |          typeobj: The data type to call this function on when both values
     |                  are of the same type in assertEqual().
     |          function: The callable taking two arguments and an optional
     |                  msg= argument that raises self.failureException with a
     |                  useful error message when the two arguments are not equal.
     |  
     |  assertAlmostEqual(self, first, second, places=None, msg=None, delta=None)
     |      Fail if the two objects are unequal as determined by their
     |      difference rounded to the given number of decimal places
     |      (default 7) and comparing to zero, or by comparing that the
     |      difference between the two objects is more than the given
     |      delta.
     |      
     |      Note that decimal places (from zero) are usually not the same
     |      as significant digits (measured from the most significant digit).
     |      
     |      If the two objects compare equal then they will automatically
     |      compare almost equal.
     |  
     |  assertAlmostEquals = deprecated_func(*args, **kwargs)
     |  
     |  assertCountEqual(self, first, second, msg=None)
     |      An unordered sequence comparison asserting that the same elements,
     |      regardless of order.  If the same element occurs more than once,
     |      it verifies that the elements occur the same number of times.
     |      
     |          self.assertEqual(Counter(list(first)),
     |                           Counter(list(second)))
     |      
     |       Example:
     |          - [0, 1, 1] and [1, 0, 1] compare equal.
     |          - [0, 0, 1] and [0, 1] compare unequal.
     |  
     |  assertDictContainsSubset(self, subset, dictionary, msg=None)
     |      Checks whether dictionary is a superset of subset.
     |  
     |  assertDictEqual(self, d1, d2, msg=None)
     |  
     |  assertEqual(self, first, second, msg=None)
     |      Fail if the two objects are unequal as determined by the '=='
     |      operator.
     |  
     |  assertEquals = deprecated_func(*args, **kwargs)
     |  
     |  assertFalse(self, expr, msg=None)
     |      Check that the expression is false.
     |  
     |  assertGreater(self, a, b, msg=None)
     |      Just like self.assertTrue(a > b), but with a nicer default message.
     |  
     |  assertGreaterEqual(self, a, b, msg=None)
     |      Just like self.assertTrue(a >= b), but with a nicer default message.
     |  
     |  assertIn(self, member, container, msg=None)
     |      Just like self.assertTrue(a in b), but with a nicer default message.
     |  
     |  assertIs(self, expr1, expr2, msg=None)
     |      Just like self.assertTrue(a is b), but with a nicer default message.
     |  
     |  assertIsInstance(self, obj, cls, msg=None)
     |      Same as self.assertTrue(isinstance(obj, cls)), with a nicer
     |      default message.
     |  
     |  assertIsNone(self, obj, msg=None)
     |      Same as self.assertTrue(obj is None), with a nicer default message.
     |  
     |  assertIsNot(self, expr1, expr2, msg=None)
     |      Just like self.assertTrue(a is not b), but with a nicer default message.
     |  
     |  assertIsNotNone(self, obj, msg=None)
     |      Included for symmetry with assertIsNone.
     |  
     |  assertLess(self, a, b, msg=None)
     |      Just like self.assertTrue(a < b), but with a nicer default message.
     |  
     |  assertLessEqual(self, a, b, msg=None)
     |      Just like self.assertTrue(a <= b), but with a nicer default message.
     |  
     |  assertListEqual(self, list1, list2, msg=None)
     |      A list-specific equality assertion.
     |      
     |      Args:
     |          list1: The first list to compare.
     |          list2: The second list to compare.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |  
     |  assertLogs(self, logger=None, level=None)
     |      Fail unless a log message of level *level* or higher is emitted
     |      on *logger_name* or its children.  If omitted, *level* defaults to
     |      INFO and *logger* defaults to the root logger.
     |      
     |      This method must be used as a context manager, and will yield
     |      a recording object with two attributes: `output` and `records`.
     |      At the end of the context manager, the `output` attribute will
     |      be a list of the matching formatted log messages and the
     |      `records` attribute will be a list of the corresponding LogRecord
     |      objects.
     |      
     |      Example::
     |      
     |          with self.assertLogs('foo', level='INFO') as cm:
     |              logging.getLogger('foo').info('first message')
     |              logging.getLogger('foo.bar').error('second message')
     |          self.assertEqual(cm.output, ['INFO:foo:first message',
     |                                       'ERROR:foo.bar:second message'])
     |  
     |  assertMultiLineEqual(self, first, second, msg=None)
     |      Assert that two multi-line strings are equal.
     |  
     |  assertNotAlmostEqual(self, first, second, places=None, msg=None, delta=None)
     |      Fail if the two objects are equal as determined by their
     |      difference rounded to the given number of decimal places
     |      (default 7) and comparing to zero, or by comparing that the
     |      difference between the two objects is less than the given delta.
     |      
     |      Note that decimal places (from zero) are usually not the same
     |      as significant digits (measured from the most significant digit).
     |      
     |      Objects that are equal automatically fail.
     |  
     |  assertNotAlmostEquals = deprecated_func(*args, **kwargs)
     |  
     |  assertNotEqual(self, first, second, msg=None)
     |      Fail if the two objects are equal as determined by the '!='
     |      operator.
     |  
     |  assertNotEquals = deprecated_func(*args, **kwargs)
     |  
     |  assertNotIn(self, member, container, msg=None)
     |      Just like self.assertTrue(a not in b), but with a nicer default message.
     |  
     |  assertNotIsInstance(self, obj, cls, msg=None)
     |      Included for symmetry with assertIsInstance.
     |  
     |  assertNotRegex(self, text, unexpected_regex, msg=None)
     |      Fail the test if the text matches the regular expression.
     |  
     |  assertNotRegexpMatches = deprecated_func(*args, **kwargs)
     |  
     |  assertRaises(self, expected_exception, *args, **kwargs)
     |      Fail unless an exception of class expected_exception is raised
     |      by the callable when invoked with specified positional and
     |      keyword arguments. If a different type of exception is
     |      raised, it will not be caught, and the test case will be
     |      deemed to have suffered an error, exactly as for an
     |      unexpected exception.
     |      
     |      If called with the callable and arguments omitted, will return a
     |      context object used like this::
     |      
     |           with self.assertRaises(SomeException):
     |               do_something()
     |      
     |      An optional keyword argument 'msg' can be provided when assertRaises
     |      is used as a context object.
     |      
     |      The context manager keeps a reference to the exception as
     |      the 'exception' attribute. This allows you to inspect the
     |      exception after the assertion::
     |      
     |          with self.assertRaises(SomeException) as cm:
     |              do_something()
     |          the_exception = cm.exception
     |          self.assertEqual(the_exception.error_code, 3)
     |  
     |  assertRaisesRegex(self, expected_exception, expected_regex, *args, **kwargs)
     |      Asserts that the message in a raised exception matches a regex.
     |      
     |      Args:
     |          expected_exception: Exception class expected to be raised.
     |          expected_regex: Regex (re.Pattern object or string) expected
     |                  to be found in error message.
     |          args: Function to be called and extra positional args.
     |          kwargs: Extra kwargs.
     |          msg: Optional message used in case of failure. Can only be used
     |                  when assertRaisesRegex is used as a context manager.
     |  
     |  assertRaisesRegexp = deprecated_func(*args, **kwargs)
     |  
     |  assertRegex(self, text, expected_regex, msg=None)
     |      Fail the test unless the text matches the regular expression.
     |  
     |  assertRegexpMatches = deprecated_func(*args, **kwargs)
     |  
     |  assertSequenceEqual(self, seq1, seq2, msg=None, seq_type=None)
     |      An equality assertion for ordered sequences (like lists and tuples).
     |      
     |      For the purposes of this function, a valid ordered sequence type is one
     |      which can be indexed, has a length, and has an equality operator.
     |      
     |      Args:
     |          seq1: The first sequence to compare.
     |          seq2: The second sequence to compare.
     |          seq_type: The expected datatype of the sequences, or None if no
     |                  datatype should be enforced.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |  
     |  assertSetEqual(self, set1, set2, msg=None)
     |      A set-specific equality assertion.
     |      
     |      Args:
     |          set1: The first set to compare.
     |          set2: The second set to compare.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |      
     |      assertSetEqual uses ducktyping to support different types of sets, and
     |      is optimized for sets specifically (parameters must support a
     |      difference method).
     |  
     |  assertTrue(self, expr, msg=None)
     |      Check that the expression is true.
     |  
     |  assertTupleEqual(self, tuple1, tuple2, msg=None)
     |      A tuple-specific equality assertion.
     |      
     |      Args:
     |          tuple1: The first tuple to compare.
     |          tuple2: The second tuple to compare.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |  
     |  assertWarns(self, expected_warning, *args, **kwargs)
     |      Fail unless a warning of class warnClass is triggered
     |      by the callable when invoked with specified positional and
     |      keyword arguments.  If a different type of warning is
     |      triggered, it will not be handled: depending on the other
     |      warning filtering rules in effect, it might be silenced, printed
     |      out, or raised as an exception.
     |      
     |      If called with the callable and arguments omitted, will return a
     |      context object used like this::
     |      
     |           with self.assertWarns(SomeWarning):
     |               do_something()
     |      
     |      An optional keyword argument 'msg' can be provided when assertWarns
     |      is used as a context object.
     |      
     |      The context manager keeps a reference to the first matching
     |      warning as the 'warning' attribute; similarly, the 'filename'
     |      and 'lineno' attributes give you information about the line
     |      of Python code from which the warning was triggered.
     |      This allows you to inspect the warning after the assertion::
     |      
     |          with self.assertWarns(SomeWarning) as cm:
     |              do_something()
     |          the_warning = cm.warning
     |          self.assertEqual(the_warning.some_attribute, 147)
     |  
     |  assertWarnsRegex(self, expected_warning, expected_regex, *args, **kwargs)
     |      Asserts that the message in a triggered warning matches a regexp.
     |      Basic functioning is similar to assertWarns() with the addition
     |      that only warnings whose messages also match the regular expression
     |      are considered successful matches.
     |      
     |      Args:
     |          expected_warning: Warning class expected to be triggered.
     |          expected_regex: Regex (re.Pattern object or string) expected
     |                  to be found in error message.
     |          args: Function to be called and extra positional args.
     |          kwargs: Extra kwargs.
     |          msg: Optional message used in case of failure. Can only be used
     |                  when assertWarnsRegex is used as a context manager.
     |  
     |  assert_ = deprecated_func(*args, **kwargs)
     |  
     |  countTestCases(self)
     |  
     |  debug(self)
     |      Run the test without collecting errors in a TestResult
     |  
     |  defaultTestResult(self)
     |  
     |  doCleanups(self)
     |      Execute all cleanup functions. Normally called for you after
     |      tearDown.
     |  
     |  fail(self, msg=None)
     |      Fail immediately, with the given message.
     |  
     |  failIf = deprecated_func(*args, **kwargs)
     |  
     |  failIfAlmostEqual = deprecated_func(*args, **kwargs)
     |  
     |  failIfEqual = deprecated_func(*args, **kwargs)
     |  
     |  failUnless = deprecated_func(*args, **kwargs)
     |  
     |  failUnlessAlmostEqual = deprecated_func(*args, **kwargs)
     |  
     |  failUnlessEqual = deprecated_func(*args, **kwargs)
     |  
     |  failUnlessRaises = deprecated_func(*args, **kwargs)
     |  
     |  id(self)
     |  
     |  run(self, result=None)
     |  
     |  setUp(self)
     |      Hook method for setting up the test fixture before exercising it.
     |  
     |  shortDescription(self)
     |      Returns a one-line description of the test, or None if no
     |      description has been provided.
     |      
     |      The default implementation of this method returns the first line of
     |      the specified test method's docstring.
     |  
     |  skipTest(self, reason)
     |      Skip this test.
     |  
     |  subTest(self, msg=<object object at 0x101140eb0>, **params)
     |      Return a context manager that will return the enclosed block
     |      of code in a subtest identified by the optional message and
     |      keyword parameters.  A failure in the subtest marks the test
     |      case as failed but resumes execution at the end of the enclosed
     |      block, allowing further test code to be executed.
     |  
     |  tearDown(self)
     |      Hook method for deconstructing the test fixture after testing it.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from unittest.case.TestCase:
     |  
     |  setUpClass() from builtins.type
     |      Hook method for setting up class fixture before running tests in the class.
     |  
     |  tearDownClass() from builtins.type
     |      Hook method for deconstructing the class fixture after running all tests in the class.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from unittest.case.TestCase:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from unittest.case.TestCase:
     |  
     |  failureException = <class 'AssertionError'>
     |      Assertion failed.
     |  
     |  longMessage = True
     |  
     |  maxDiff = 640
    
    class TestTemperature(unittest.case.TestCase)
     |  TestTemperature(methodName='runTest')
     |  
     |  A class whose instances are single test cases.
     |  
     |  By default, the test code itself should be placed in a method named
     |  'runTest'.
     |  
     |  If the fixture may be used for many test cases, create as
     |  many test methods as are needed. When instantiating such a TestCase
     |  subclass, specify in the constructor arguments the name of the test method
     |  that the instance is to execute.
     |  
     |  Test authors should subclass TestCase for their own tests. Construction
     |  and deconstruction of the test's environment ('fixture') can be
     |  implemented by overriding the 'setUp' and 'tearDown' methods respectively.
     |  
     |  If it is necessary to override the __init__ method, the base class
     |  __init__ method must always be called. It is important that subclasses
     |  should not change the signature of their __init__ method, since instances
     |  of the classes are instantiated automatically by parts of the framework
     |  in order to be run.
     |  
     |  When subclassing TestCase, you can set these attributes:
     |  * failureException: determines which exception will be raised when
     |      the instance's assertion methods fail; test methods raising this
     |      exception will be deemed to have 'failed' rather than 'errored'.
     |  * longMessage: determines whether long messages (including repr of
     |      objects used in assert methods) will be printed on failure in *addition*
     |      to any explicit message passed.
     |  * maxDiff: sets the maximum length of a diff in failure messages
     |      by assert methods using difflib. It is looked up as an instance
     |      attribute so can be configured by individual tests if required.
     |  
     |  Method resolution order:
     |      TestTemperature
     |      unittest.case.TestCase
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  test_Kelvin(self)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from unittest.case.TestCase:
     |  
     |  __call__(self, *args, **kwds)
     |      Call self as a function.
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  __hash__(self)
     |      Return hash(self).
     |  
     |  __init__(self, methodName='runTest')
     |      Create an instance of the class that will use the named test
     |      method when executed. Raises a ValueError if the instance does
     |      not have a method with the specified name.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  addCleanup(*args, **kwargs)
     |      Add a function, with arguments, to be called when the test is
     |      completed. Functions added are called on a LIFO basis and are
     |      called after tearDown on test failure or success.
     |      
     |      Cleanup items are called even if setUp fails (unlike tearDown).
     |  
     |  addTypeEqualityFunc(self, typeobj, function)
     |      Add a type specific assertEqual style function to compare a type.
     |      
     |      This method is for use by TestCase subclasses that need to register
     |      their own type equality functions to provide nicer error messages.
     |      
     |      Args:
     |          typeobj: The data type to call this function on when both values
     |                  are of the same type in assertEqual().
     |          function: The callable taking two arguments and an optional
     |                  msg= argument that raises self.failureException with a
     |                  useful error message when the two arguments are not equal.
     |  
     |  assertAlmostEqual(self, first, second, places=None, msg=None, delta=None)
     |      Fail if the two objects are unequal as determined by their
     |      difference rounded to the given number of decimal places
     |      (default 7) and comparing to zero, or by comparing that the
     |      difference between the two objects is more than the given
     |      delta.
     |      
     |      Note that decimal places (from zero) are usually not the same
     |      as significant digits (measured from the most significant digit).
     |      
     |      If the two objects compare equal then they will automatically
     |      compare almost equal.
     |  
     |  assertAlmostEquals = deprecated_func(*args, **kwargs)
     |  
     |  assertCountEqual(self, first, second, msg=None)
     |      An unordered sequence comparison asserting that the same elements,
     |      regardless of order.  If the same element occurs more than once,
     |      it verifies that the elements occur the same number of times.
     |      
     |          self.assertEqual(Counter(list(first)),
     |                           Counter(list(second)))
     |      
     |       Example:
     |          - [0, 1, 1] and [1, 0, 1] compare equal.
     |          - [0, 0, 1] and [0, 1] compare unequal.
     |  
     |  assertDictContainsSubset(self, subset, dictionary, msg=None)
     |      Checks whether dictionary is a superset of subset.
     |  
     |  assertDictEqual(self, d1, d2, msg=None)
     |  
     |  assertEqual(self, first, second, msg=None)
     |      Fail if the two objects are unequal as determined by the '=='
     |      operator.
     |  
     |  assertEquals = deprecated_func(*args, **kwargs)
     |  
     |  assertFalse(self, expr, msg=None)
     |      Check that the expression is false.
     |  
     |  assertGreater(self, a, b, msg=None)
     |      Just like self.assertTrue(a > b), but with a nicer default message.
     |  
     |  assertGreaterEqual(self, a, b, msg=None)
     |      Just like self.assertTrue(a >= b), but with a nicer default message.
     |  
     |  assertIn(self, member, container, msg=None)
     |      Just like self.assertTrue(a in b), but with a nicer default message.
     |  
     |  assertIs(self, expr1, expr2, msg=None)
     |      Just like self.assertTrue(a is b), but with a nicer default message.
     |  
     |  assertIsInstance(self, obj, cls, msg=None)
     |      Same as self.assertTrue(isinstance(obj, cls)), with a nicer
     |      default message.
     |  
     |  assertIsNone(self, obj, msg=None)
     |      Same as self.assertTrue(obj is None), with a nicer default message.
     |  
     |  assertIsNot(self, expr1, expr2, msg=None)
     |      Just like self.assertTrue(a is not b), but with a nicer default message.
     |  
     |  assertIsNotNone(self, obj, msg=None)
     |      Included for symmetry with assertIsNone.
     |  
     |  assertLess(self, a, b, msg=None)
     |      Just like self.assertTrue(a < b), but with a nicer default message.
     |  
     |  assertLessEqual(self, a, b, msg=None)
     |      Just like self.assertTrue(a <= b), but with a nicer default message.
     |  
     |  assertListEqual(self, list1, list2, msg=None)
     |      A list-specific equality assertion.
     |      
     |      Args:
     |          list1: The first list to compare.
     |          list2: The second list to compare.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |  
     |  assertLogs(self, logger=None, level=None)
     |      Fail unless a log message of level *level* or higher is emitted
     |      on *logger_name* or its children.  If omitted, *level* defaults to
     |      INFO and *logger* defaults to the root logger.
     |      
     |      This method must be used as a context manager, and will yield
     |      a recording object with two attributes: `output` and `records`.
     |      At the end of the context manager, the `output` attribute will
     |      be a list of the matching formatted log messages and the
     |      `records` attribute will be a list of the corresponding LogRecord
     |      objects.
     |      
     |      Example::
     |      
     |          with self.assertLogs('foo', level='INFO') as cm:
     |              logging.getLogger('foo').info('first message')
     |              logging.getLogger('foo.bar').error('second message')
     |          self.assertEqual(cm.output, ['INFO:foo:first message',
     |                                       'ERROR:foo.bar:second message'])
     |  
     |  assertMultiLineEqual(self, first, second, msg=None)
     |      Assert that two multi-line strings are equal.
     |  
     |  assertNotAlmostEqual(self, first, second, places=None, msg=None, delta=None)
     |      Fail if the two objects are equal as determined by their
     |      difference rounded to the given number of decimal places
     |      (default 7) and comparing to zero, or by comparing that the
     |      difference between the two objects is less than the given delta.
     |      
     |      Note that decimal places (from zero) are usually not the same
     |      as significant digits (measured from the most significant digit).
     |      
     |      Objects that are equal automatically fail.
     |  
     |  assertNotAlmostEquals = deprecated_func(*args, **kwargs)
     |  
     |  assertNotEqual(self, first, second, msg=None)
     |      Fail if the two objects are equal as determined by the '!='
     |      operator.
     |  
     |  assertNotEquals = deprecated_func(*args, **kwargs)
     |  
     |  assertNotIn(self, member, container, msg=None)
     |      Just like self.assertTrue(a not in b), but with a nicer default message.
     |  
     |  assertNotIsInstance(self, obj, cls, msg=None)
     |      Included for symmetry with assertIsInstance.
     |  
     |  assertNotRegex(self, text, unexpected_regex, msg=None)
     |      Fail the test if the text matches the regular expression.
     |  
     |  assertNotRegexpMatches = deprecated_func(*args, **kwargs)
     |  
     |  assertRaises(self, expected_exception, *args, **kwargs)
     |      Fail unless an exception of class expected_exception is raised
     |      by the callable when invoked with specified positional and
     |      keyword arguments. If a different type of exception is
     |      raised, it will not be caught, and the test case will be
     |      deemed to have suffered an error, exactly as for an
     |      unexpected exception.
     |      
     |      If called with the callable and arguments omitted, will return a
     |      context object used like this::
     |      
     |           with self.assertRaises(SomeException):
     |               do_something()
     |      
     |      An optional keyword argument 'msg' can be provided when assertRaises
     |      is used as a context object.
     |      
     |      The context manager keeps a reference to the exception as
     |      the 'exception' attribute. This allows you to inspect the
     |      exception after the assertion::
     |      
     |          with self.assertRaises(SomeException) as cm:
     |              do_something()
     |          the_exception = cm.exception
     |          self.assertEqual(the_exception.error_code, 3)
     |  
     |  assertRaisesRegex(self, expected_exception, expected_regex, *args, **kwargs)
     |      Asserts that the message in a raised exception matches a regex.
     |      
     |      Args:
     |          expected_exception: Exception class expected to be raised.
     |          expected_regex: Regex (re.Pattern object or string) expected
     |                  to be found in error message.
     |          args: Function to be called and extra positional args.
     |          kwargs: Extra kwargs.
     |          msg: Optional message used in case of failure. Can only be used
     |                  when assertRaisesRegex is used as a context manager.
     |  
     |  assertRaisesRegexp = deprecated_func(*args, **kwargs)
     |  
     |  assertRegex(self, text, expected_regex, msg=None)
     |      Fail the test unless the text matches the regular expression.
     |  
     |  assertRegexpMatches = deprecated_func(*args, **kwargs)
     |  
     |  assertSequenceEqual(self, seq1, seq2, msg=None, seq_type=None)
     |      An equality assertion for ordered sequences (like lists and tuples).
     |      
     |      For the purposes of this function, a valid ordered sequence type is one
     |      which can be indexed, has a length, and has an equality operator.
     |      
     |      Args:
     |          seq1: The first sequence to compare.
     |          seq2: The second sequence to compare.
     |          seq_type: The expected datatype of the sequences, or None if no
     |                  datatype should be enforced.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |  
     |  assertSetEqual(self, set1, set2, msg=None)
     |      A set-specific equality assertion.
     |      
     |      Args:
     |          set1: The first set to compare.
     |          set2: The second set to compare.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |      
     |      assertSetEqual uses ducktyping to support different types of sets, and
     |      is optimized for sets specifically (parameters must support a
     |      difference method).
     |  
     |  assertTrue(self, expr, msg=None)
     |      Check that the expression is true.
     |  
     |  assertTupleEqual(self, tuple1, tuple2, msg=None)
     |      A tuple-specific equality assertion.
     |      
     |      Args:
     |          tuple1: The first tuple to compare.
     |          tuple2: The second tuple to compare.
     |          msg: Optional message to use on failure instead of a list of
     |                  differences.
     |  
     |  assertWarns(self, expected_warning, *args, **kwargs)
     |      Fail unless a warning of class warnClass is triggered
     |      by the callable when invoked with specified positional and
     |      keyword arguments.  If a different type of warning is
     |      triggered, it will not be handled: depending on the other
     |      warning filtering rules in effect, it might be silenced, printed
     |      out, or raised as an exception.
     |      
     |      If called with the callable and arguments omitted, will return a
     |      context object used like this::
     |      
     |           with self.assertWarns(SomeWarning):
     |               do_something()
     |      
     |      An optional keyword argument 'msg' can be provided when assertWarns
     |      is used as a context object.
     |      
     |      The context manager keeps a reference to the first matching
     |      warning as the 'warning' attribute; similarly, the 'filename'
     |      and 'lineno' attributes give you information about the line
     |      of Python code from which the warning was triggered.
     |      This allows you to inspect the warning after the assertion::
     |      
     |          with self.assertWarns(SomeWarning) as cm:
     |              do_something()
     |          the_warning = cm.warning
     |          self.assertEqual(the_warning.some_attribute, 147)
     |  
     |  assertWarnsRegex(self, expected_warning, expected_regex, *args, **kwargs)
     |      Asserts that the message in a triggered warning matches a regexp.
     |      Basic functioning is similar to assertWarns() with the addition
     |      that only warnings whose messages also match the regular expression
     |      are considered successful matches.
     |      
     |      Args:
     |          expected_warning: Warning class expected to be triggered.
     |          expected_regex: Regex (re.Pattern object or string) expected
     |                  to be found in error message.
     |          args: Function to be called and extra positional args.
     |          kwargs: Extra kwargs.
     |          msg: Optional message used in case of failure. Can only be used
     |                  when assertWarnsRegex is used as a context manager.
     |  
     |  assert_ = deprecated_func(*args, **kwargs)
     |  
     |  countTestCases(self)
     |  
     |  debug(self)
     |      Run the test without collecting errors in a TestResult
     |  
     |  defaultTestResult(self)
     |  
     |  doCleanups(self)
     |      Execute all cleanup functions. Normally called for you after
     |      tearDown.
     |  
     |  fail(self, msg=None)
     |      Fail immediately, with the given message.
     |  
     |  failIf = deprecated_func(*args, **kwargs)
     |  
     |  failIfAlmostEqual = deprecated_func(*args, **kwargs)
     |  
     |  failIfEqual = deprecated_func(*args, **kwargs)
     |  
     |  failUnless = deprecated_func(*args, **kwargs)
     |  
     |  failUnlessAlmostEqual = deprecated_func(*args, **kwargs)
     |  
     |  failUnlessEqual = deprecated_func(*args, **kwargs)
     |  
     |  failUnlessRaises = deprecated_func(*args, **kwargs)
     |  
     |  id(self)
     |  
     |  run(self, result=None)
     |  
     |  setUp(self)
     |      Hook method for setting up the test fixture before exercising it.
     |  
     |  shortDescription(self)
     |      Returns a one-line description of the test, or None if no
     |      description has been provided.
     |      
     |      The default implementation of this method returns the first line of
     |      the specified test method's docstring.
     |  
     |  skipTest(self, reason)
     |      Skip this test.
     |  
     |  subTest(self, msg=<object object at 0x101140eb0>, **params)
     |      Return a context manager that will return the enclosed block
     |      of code in a subtest identified by the optional message and
     |      keyword parameters.  A failure in the subtest marks the test
     |      case as failed but resumes execution at the end of the enclosed
     |      block, allowing further test code to be executed.
     |  
     |  tearDown(self)
     |      Hook method for deconstructing the test fixture after testing it.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from unittest.case.TestCase:
     |  
     |  setUpClass() from builtins.type
     |      Hook method for setting up class fixture before running tests in the class.
     |  
     |  tearDownClass() from builtins.type
     |      Hook method for deconstructing the class fixture after running all tests in the class.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from unittest.case.TestCase:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from unittest.case.TestCase:
     |  
     |  failureException = <class 'AssertionError'>
     |      Assertion failed.
     |  
     |  longMessage = True
     |  
     |  maxDiff = 640

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    dewpoint(T, RH)
        Calculate dewpoint temperature given relative humidity and temperative (all temperature in Celcius)
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(x, y, /)
        greatest common divisor of x and y
    
    humidity(T, DP)
        Calculate relative humidity given temperative and dewpoint temperature (all temperature in Celcius)
    
    hypot(x, y, /)
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    temperature(RH, DP)
        Calculate temperative given relative humidity and dewpoint temperature (all temperature in Celcius)
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    /Volumes/DATA/GitHub/psychrometric/source/psychrometric.py


