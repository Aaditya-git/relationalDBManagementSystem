import json

f = open("inputCol.json" ,)

data = json.load(f)

for i in data:
    print(data[i])

f.close()
