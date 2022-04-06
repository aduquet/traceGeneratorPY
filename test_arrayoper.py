from audioop import add
import unittest
from inspect import formatargspec, getfullargspec, signature
import inspect
from arrayoper import *
from tracegen import *

# class TestArrayoper(unittest.TestCase):
#     def test_volume(self):
#         print('++++++++++++++++++++++++++++++++++++')
#         # print('****',inspect.getfullargspec(add))
#         # print('****',inspect.signature(add))
#         myClass = Array_oper([1,2,3],[1,2,3])
#         sys.settrace(trace_calls_and_returns)
#         myClass.add()
#         print('************************************')
#     # def test_sub(self):
#     #     print('++++++++++++++++++++++++++++++++++++')
#     #     myClass = Array_oper([1,2,3],[1,2,3])
#     #     # sys.settrace(trace_calls_and_returns)
#     #     myClass.sub()
#     #     print('************************************')
#     #     # self.assertAlmostEqual(cuboid_volume(2),8)
#     #     # self.assertAlmostEqual(cuboid_volume(1),1)
#     #     # self.assertAlmostEqual(cuboid_volume(0),0)
#     #     # self.assertAlmostEqual(cuboid_volume(5.5),166.375)    
    

myClass = Array_oper([1,2,3],[1,2,3])
sys.settrace(trace_calls_and_returns)
myClass.add()



