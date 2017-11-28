def multiplication_table():
    print "x  1  2  3  4  5  6  7  8  9  10  11  12"
    for x in range(1, 13):
        x_axis = ""
        for y in range(0, 13):
            if y is 0:
                x_axis += ""+str(x)
            else:
                x_axis += "  "+str(y*x)
        print x_axis      
        

multiplication_table()