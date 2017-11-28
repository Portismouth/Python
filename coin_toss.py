from random import random

def coin_toss():
    count_heads = 0
    count_tails = 0
    for num in range(1, 5001):
        x = random()
        y = random()
        if x > y:
            count_heads += 1
            print "Attempt #"+str(num)+": Throwing a coin... It's heads!... Got "+str(count_heads)+" heads and "+str(count_tails)+" tails so far"
        else:
            count_tails +=1
            print "Attempt #" + str(num) + ": Throwing a coin... It's tails!... Got " + str(count_tails) + " heads and "+str(count_heads)+" tails so far"

coin_toss()
