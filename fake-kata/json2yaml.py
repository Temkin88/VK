import yaml
import json

with open('swagger.yml', 'w') as y:
    with open('openapi.json', 'rb') as f:
        yaml.dump(json.load(f), y)
