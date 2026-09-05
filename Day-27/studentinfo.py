import json
'''with open("data.json",'r') as file:
    data = json.load(file)
data["username"]="harsha"
data["skills"].append("sql")
with open("data.json",'w') as file:
    json.dump(data,file,indent=4)'''
student={
    "name":"harsha",
    "age":23,
    "course": "python"
    }
json_data=json.dumps(student)
print(json_data)
student=json.loads(json_data)
print(student)
print(type(student))