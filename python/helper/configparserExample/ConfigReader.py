from configparser import ConfigParser


class ConfigReader:

    configuration = ConfigParser()

    def __init__(self):
        self.configuration.read("config.ini")

    def get_config_by_key(self, section, key, default):
        if section in self.configuration:
            return self.configuration[section][key]
        else:
            return default
