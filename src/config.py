import json

config = dict()

def init():
    file = open('./config/config.json', 'r')
    global config
    config = json.loads(file.read())
    file.close()
    
def save():
    file = open('./config/config.json', 'w')
    global config
    config = json.dumps(config, indent=4)
    file.write(config)
    file.close()
    
def get_value(key):
    global config
    value = config[key]
    return value
    
def set_value(key, value):
    global config
    config[key] = value