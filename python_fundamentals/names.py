# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]

# for i in range(0, len(students)):
#     print students[i]["first_name"], students[i]["last_name"]

users = {
    'Students': [
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}

for i in users:
    counter = 0
    print i
    for p in users[i]:
        counter += 1
        first_name = p["first_name"]
        last_name = p["last_name"]
        print str(counter),"-",first_name, last_name,"-", len(first_name)+len(last_name)


