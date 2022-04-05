import os
import pathlib
import glob as gl
import numpy as np
import pandas as pd
from arrayoper import *

a = []
# b = ['a',' d', 'v']
b = [1,2,3]

# Array_oper(a)
# Array_oper(b)
myClass = Array_oper(a,b)
myClass.printArray()
print('add', myClass.add())
print('sub', myClass.sub())
print('dot_product', myClass.dot_product())