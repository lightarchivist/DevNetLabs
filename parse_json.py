import json

json_data = open ('data.json', r)
data = json.load(json_data)
json_data.close()
print(data) 
