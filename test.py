import json

center = 100
radius = 500

data = {
    'Raidus' : radius,
    'Center' : center
}

# json_str = json.dumps(data)

# Writing JSON data
with open('data.json', 'w') as f:
     json.dump(data, f)
