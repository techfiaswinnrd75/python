'''
Student: Marks
Aswin  : 50
Appu   : 40
....

'''


d = {}
d = {
    "Key1": "Value1",
    "Key2": "Value2"
}

# Keys should not be a mutable data type...

# print(d)

student = {
    "Name": "Aswin",
    "Marks": 50,
    "Roll Number": 22
}

print(student["Name"])

for i in student:
    # print(i)
    pass

print(student.get("Mark", 10))

student["Name"] = "Aswin P"
print(student)

student.update({"Name": "Aswin", "Marks": 70})
print(student)

print(student.pop("Marks"))
print(student)

print(student.keys())
print(student.values())
print(student.items())


