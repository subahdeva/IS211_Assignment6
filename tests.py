#!/usr/bin/env python
# coding: utf-8

# In[10]:



import unittest

import conversions
import conversions_refactored


class ConversionTests(unittest.TestCase):
    
    hr = '---------------------------'

    temp_values = (
        {'celsius': 300.00,
         'fahrenheit': 572.00,
         'kelvin': 573.15},
        {'celsius': 290.00,
         'fahrenheit': 554.00,
         'kelvin': 563.15},
        {'celsius': 210.00,
         'fahrenheit': 410.00,
         'kelvin': 483.15},
        {'celsius': 170.00,
         'fahrenheit': 338.00,
         'kelvin': 443.15},
        {'celsius': 140.00,
         'fahrenheit': 284.00,
         'kelvin': 413.15},
        {'celsius': 100.00,
         'fahrenheit': 212.00,
         'kelvin': 373.15}
    )

    dist_values = (
        {'mile': 1.0,
         'yard': 1760.0,
         'meter': 1609.344},
        {'mile': 32.654,
         'yard': 57471.04,
         'meter': 52551.519},
        {'mile': 0.0321,
         'yard': 56.5,
         'meter': 51.664},
        {'mile': 0.062,
         'yard': 109.361,
         'meter': 100.0},
        {'mile': 0.170,
         'yard': 300.0,
         'meter': 274.336j}
    )

    def test_convert(self):
        tmp_keys = self.temp_values[0].keys()
        dst_keys = self.dist_values[0].keys()
        print 'conversions_refactored.convert() - Conversions test:'
        for x in xrange(100):
            if x % 2:
                from_unit = random.choice(tmp_keys)
                to_unit = random.choice(tmp_keys)
                testme = self.temp_values
                print 'Testing temperature conversion:'
            else:
                from_unit = random.choice(dst_keys)
                to_unit = random.choice(dst_keys)
                testme = self.dist_values
                print 'Testing length conversion'
            for row in testme:
                result = ref.convert(from_unit, to_unit, row[from_unit])
                print self.hr
                print 'Input Unit: ', from_unit.title()
                print 'Output Unit: ', to_unit.title()
                print 'Input Value: ', row[from_unit]
                print 'Output value: ', result
                print 'Expected Value: ', row[to_unit]
                self.assertAlmostEqual(row[to_unit], result, 1)

    def test_convert_exception(self):
        print 'conversions_refactored.convert() - Exception test:'
        tmp_keys = self.temp_values[0].keys()
        dst_keys = self.dist_values[0].keys()

        for x in xrange(10):
            from_unit = random.choice(tmp_keys)
            to_unit = random.choice(dst_keys)
            print self.hr
            print 'Input Unit: ', from_unit.title()
            print 'Output Unit: ', to_unit.title()
            print 'Value: ', 100.5
            self.assertRaises(ref.InvalidConversion,
                              ref.convert, from_unit, to_unit, 100.5)

    def test_fahr_to_celsius(self):
        print "Testing fahr_to_celsius"
        for row in self.temp_values:
            result = convert.fahr_to_celsius(row['fahrenheit'])
            print self.hr
            print 'Input Fahr = ', row['fahrenheit']
            print 'Output Celsius = ', result
            print 'Expected Celsius = ', row['celsius']
            self.assertAlmostEqual(row['celsius'], result)

    def test_fahr_to_kelvin(self):
        print "Testing fahr_to_kelvin"
        for row in self.temp_values:
            result = convert.fahr_to_kelvin(row['fahrenheit'])
            print self.hr
            print 'Input Fahr = ', row['fahrenheit']
            print 'Output Kelvin = ', result
            print 'Expected Kelvin = ', row['kelvin']
            self.assertAlmostEqual(row['kelvin'], result)

    def test_celsius_to_fahr(self):
        print "Testing celsius_to_fahr"
        for row in self.temp_values:
            result = convert.celsius_to_fahr(row['celsius'])
            print self.hr
            print 'Input Celsius = ', row['celsius']
            print 'Output Fahr = ', result
            print 'Expected Fahr = ', row['fahrenheit']
            self.assertAlmostEqual(row['fahrenheit'], result)

    def test_celsius_to_kelvin(self):
        print 'Testing celsius_to_kelvin'
        for row in self.temp_values:
            result = convert.celsius_to_kelvin(row['celsius'])
            print self.hr
            print 'Input Celsius = ', row['celsius']
            print 'Output Kelvin = ', result
            print 'Expected Fahr = ', row['kelvin']
            self.assertAlmostEqual(row['kelvin'], result)

    def test_kelvin_to_fahr(self):
        print 'Testing kelvin_to_fahr'
        for row in self.temp_values:
            result = convert.kelvin_to_fahr(row['kelvin'])
            print self.hr
            print 'Input Kelvin = ', row['kelvin']
            print 'Output Fahr = ', result
            print 'Expected Fahr = ', row['fahrenheit']
            self.assertAlmostEqual(row['fahrenheit'], result)

    def test_kelvin_to_celsius(self):
        print 'Testing kelvin_to_celsius'
        for row in self.temp_values:
            result = convert.kelvin_to_celsius(row['kelvin'])
            print self.hr
            print 'Input Kelvin = ', row['kelvin']
            print 'Output Celsius = ', result
            print 'Expected Celsius = ', row['celsius']
            self.assertAlmostEqual(row['celsius'], result)


if __name__ == '__main__':
    unittest.main()


# In[ ]:





# In[ ]:




