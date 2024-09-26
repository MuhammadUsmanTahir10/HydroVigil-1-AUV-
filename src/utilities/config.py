# src/utilities/config.py

import json

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file

    def load_config(self):
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        return config
