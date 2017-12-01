mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]

def get_list_type(lst):
    new_str = ""
    total = 0

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_str += value

    if new_str and total:
        print "The list you entered is of mixed type"
        print "String :", new_str
        print "Sum: ", total

    elif total:
        print "The list you entered is of integer type"
        print "Sum: ", total

    elif new_str:
        print "The list you entered is of string type"
        print "String: ", new_str

get_list_type(string_list)