from ast import Return
from sympy import false, true


class Array_oper(object):
    
    def __init__(self, a, b):
        self.array_a = a 
        self.array_b = b
        
    def printArray(self):
        print(self.array_a, '\n')
        print(self.array_b, '\n')
        
    def add(self):
        
        if self.equalSize():
            sum = [x + y for x, y in zip(self.array_a, self.array_b)]
            return sum
        else:
            return 'arrays must have the same size'
        
    def sub(self):
        
        if self.equalSize():
            diff = [x - y for x, y in zip(self.array_a, self.array_b)]
            
            return diff
        else:
            return 'arrays must have the same size'
        
    def dot_product(self):
        dp = 0
        if self.equalSize():
            for i in range(len(self.array_a)):
                dp += (self.array_a[i] * self.array_b[i])
            # print(self.isEmpty(true))
            return dp
        else:
            return 'arrays must have the same size'
            
    def isEmpty(self, is_a):
        
        if is_a:
            if len(self.array_a):
                return false 
            else:
                return true
        else:
            if len(self.array_b):
                return false
            else:
                return true
                
        # return len(self.array_a) if is_a else len(self.array_b)
    
    def equalSize(self):
        
        if(self.getSize(true) ==  self.getSize(false)):
            return true
        
        else:
            return false
            
    def getSize(self, is_a):
        
        return len(self.array_a) if is_a else len(self.array_b)