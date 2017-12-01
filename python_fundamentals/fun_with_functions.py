# # Odd/Even
# def odds_evens(num):
#     for x in range(1, num+1):
#         if x % 2 == 0:
#             print "Number is", str(x) + ". This is an even number."
#         else:
#             print "Number is", str(x) +". This is an odd number."

# odds_evens(2000)

#Multiply 

def multiply(arr, mult):
    op = [] #new array
    for i in arr:
        i = i * mult #multiplies elements by input
        op.append(i) #builds new array
    return op


# multiply([2, 4, 10, 16], 5)

#hacker challenge

def layered_multiples(arr):
    print arr
    new_arr = []
    for i in arr:
        l_array = []
        for l in range(0,i):
            l_array.append(1)
        new_arr.append(l_array)
    print new_arr

layered_multiples(multiply([2, 4, 5], 3))
