import json 
student1 = {
    "name":"harshita",
    "age":30,
    "city":"bhopal",
    "Marks":80
}

student2 = {
    "name":"Meena",
    "age":20,
    "city":"bhopal",
    "Marks":50
}

student3 = {
    "name":"harsha",
    "age":20,
    "city":"bhopal",
    "Marks":90
}

json_data1 = json.dumps(student1)
json_data2 = json.dumps(student2)
json_data3 = json.dumps(student3)
print(json_data1)
print(json_data2)
print(json_data3)

with open("students.json","w") as f:
    json.dump(student1,f)
    json.dump(student2,f)
    json.dump(student3,f)

print("Json file created")