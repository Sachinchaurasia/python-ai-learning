#    PYTHON-------------------> JSON


import json
data={
    "name":"Sachin",
    "role":"AI Engineer"
}

json_data=json.dumps(data)
print(json_data)

#############################################

#JSON------------------->PYTHON

json_data='''
{
    "name":"Sachin",
    "role":"AI Engineer"
    }'''

data=json.loads(json_data)
print(data)
