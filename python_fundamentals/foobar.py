def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def is_square(n):
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y:
            return False
        y.add(x)
    return True

def foo_bar():
    for n in range(100, 201):
        if is_prime(n) is True:
            print n, "Foo"
        elif is_square(n):
            print n
            # print n, "Bar"
        else:
            print "reached else statement"
            # print n, "FooBar"

foo_bar()



