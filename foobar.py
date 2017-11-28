def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def is_square(num):
    for i in range(num+1):
        if i*i == int(num/2):
            return True
    else:
        return False

def foo_bar():
    for n in range(100, 201):
        print n
        if is_prime(n) is True:
            print "reached if"
            # print n, "Foo"
        elif is_square(n):
            print "reached elif"
            # print n, "Bar"
        else:
            print "reached else statement"
            # print n, "FooBar"

foo_bar()

