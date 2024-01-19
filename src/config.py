import json

def init_config():
    file = open('./config/config.json', 'r')
    config = json.loads(file.read())
    file.close
    return config

def save_config(config):
    file = open('./config/config.json', 'w')
    new_config = json.dumps(config, indent=4)
    file.write(new_config)
    file.close
    
def get_value(key):
    config = init_config()
    value = config[key]
    return value
    
def set_value(key, value):
    file = open('./config/config.json', 'r')
    config = json.loads(file.read())
    file.close()
    file = open('./config/config.json', 'w')
    config[key] = value
    new_config = json.dumps(config, indent=4)
    file.write(new_config)
    file.close()
    print(new_config)