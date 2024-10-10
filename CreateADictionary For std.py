# create a Dictionary
Student ={"SID": 111, "Sname":"Tom", "Course": "CCDM","Age": 25}
print(Student)

# Get all key
print(Student.keys)
print(Student.values)
print(Student.items)

#update dictionary
Student.update({"Sname": "Tom"})
print(Student)