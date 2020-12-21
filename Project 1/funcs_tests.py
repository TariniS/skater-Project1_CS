import unittest
from funcs import *
import funcs

class TestCases(unittest.TestCase):
   def test_poundsToKG_1(self):
   #testing the output with multiple values, including 0's, negatives and decimal values
      self.assertAlmostEqual(poundsToKG(0), 0.0)
      self.assertEqual(poundsToKG(5),2.26796)
      self.assertEqual(poundsToKG(10),4.53592)
      self.assertEqual(poundsToKG(-2),-0.907184)
      
   def test_getMassObject_1(self):
   #testing the output with multiple values, including the 5 given letters, along with other letters
      self.assertEqual(getMassObject('t'), 0.1)
      self.assertEqual(getMassObject('p'),1.0)
      self.assertEqual(getMassObject('r'),3.0)
      self.assertEqual(getMassObject('g'),5.3)
      self.assertEqual(getMassObject('l'),9.07)
      self.assertEqual(getMassObject('k'),0.0)
      self.assertEqual(getMassObject('u'),0.0)
      
   def test_getVelocityObject_1(self):
   #testing the output with 0's, a whole number, as well as a value that outputs a decimal
      self.assertAlmostEqual(getVelocityObject(0), 0.0)
      self.assertAlmostEqual(getVelocityObject(10),7)
      self.assertAlmostEqual(getVelocityObject(20),9.8994949366)
           
   def test_getVelocitySkater_1(self):
   #testing the output with 0's, whole numbers with decimal outputs and integer outputs, as well as dividing by zero. 
      self.assertAlmostEqual(getVelocitySkater(100, 0, 100), 0.0)
      self.assertAlmostEqual(getVelocitySkater(90,50,10),5.5555555555)
      self.assertAlmostEqual(getVelocitySkater(1,20,30),600)
      self.assertRaises(ZeroDivisionError,funcs.getVelocitySkater,0,3,3)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
