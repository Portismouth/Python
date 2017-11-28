# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output

def tupleout(ur_dict):
  new_list = []
  output = ""
  for i in ur_dict:
    output = (i, my_dict[i])
    new_list.append(output)
  print new_list

tupleout(my_dict)