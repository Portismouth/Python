import itertools
import datetime

class Call(object):
    class_counter = 1
    def __init__(self, caller_name, caller_number, time, reason):
        self.caller = caller_name
        self.number = caller_number
        self.time = time
        self.reason = reason
        self.id = Call.class_counter
        Call.class_counter += 1
    def info_display(self):
        print self.id, self.caller, self.number, self.time, self.reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0
    def add(self, callx):
        self.calls.append(callx)
        self.queue += 1
        return self
    def remove(self):
        self.calls.pop(0)
        return self
    # def remove_caller(self, number):
    #     for each in self.calls:
    #         if each.number == number:
    #             self.calls.pop(each)
    def info(self):
        for each in self.calls:
            print each.caller, each.number 
        print self.queue


call1 = Call("Ozzy Gonzalez", "919-612-7729", "12:30", "General Inquiry")
call2 = Call("Jim Jenkins", "919-612-7789", "12:30", "General Inquiry")

# call1.info_display()
# call2.info_display()

cc = CallCenter()
cc.add(call1).add(call2)
cc.info()
cc.remove()
cc.info()
#print datetime.datetime.now().time()
