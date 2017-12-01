#part 1
class MathDojo(object):
    #attributes
    def __init__(self):
        self.result = 0
    #methods        
    def add(self, *num): #try adding a list as a param, then sum 
        sub_total = 0
        for i in num:
            if isinstance(i, list):
                sub_total += sum(i)
            elif isinstance(i, int):
                sub_total += i
            elif isinstance(i, tuple):
                sub_total += sum(i)
        self.result += sub_total
        return self
    def subtract(self, *num):
        sub_total = 0
        for i in num:
            if isinstance(i, list):
                sub_total += sum(i)
            elif isinstance(i, int):
                sub_total += i
            elif isinstance(i, tuple):
                sub_total += sum(i)
        self.result += sub_total
        return self
    def display_result(self):
        print self.result
        return self

md = MathDojo()

md.add([1], 3, 4).add([3, 5, 7, 8], (1,1,1),[2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).display_result()
