# sets must have immutable elements.
d={1:"stupid", 2:"not", 3:"are", 4:"you"};
#Dictionary and its OPERATIONS
Student = {"Anchal": 33, "Aman": 45,"Sanjay":89}
print(Student)
print(type(Student))
# To get an Key value by name.
print(Student.get("Anchal"))
print(Student['Anchal'])
for i in Student:
    print(i,Student[i])
    for i in Student:
        print(i)
print(len(Student))
del Student['Aman']
print(Student)
print(Student.pop('Anchal'))
print(Student.get('Sanjay'))

#Nested Dictionary


Student = { "Anchal" : { "History" : 85, "Physics" : 87, "Chemistry" : 90, "Maths" : 76 },
            "Krishna" : { "History" : 86,  "Maths" : 89, "Hindi" : 81, "English" : 84},
            "Aman" : { "History" : 87, "Hindi" : 86, "Social Science" : 83, "General Knowledge":92 }
            }
print(Student["Anchal"])
print(Student["Anchal"]["History"])
print(Student["Krishna"]["Maths"])
print(Student["Aman"]["Hindi"])
print(Student["Aman"]["General Knowledge"])
print(Student["Krishna"])
for i in Student:
    print(i,"got",Student[i]["History"],"Marks in History" )
print(len(Student))
for i in Student:
    print(i, len(Student[i]))


