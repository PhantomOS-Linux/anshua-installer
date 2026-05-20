import sys

class Config:
    system_name = None # e.g. "Anshua OS"
    image_link = None # e.g. "ghcr.io/phantomos/anshuaos:latest"

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = Config()
        self.load_config()

    # Config file format:
    # system_name=Anshua OS
    # image_link=ghcr.io/phantomos/anshuaos:latest

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                for line in f:
                    key, value = line.strip().split('=')
                    setattr(self.config, key, value)
        except Exception as e:
            print(f"Error loading config: {e}")
            sys.exit(1)

    def get_config(self):
        return self.config