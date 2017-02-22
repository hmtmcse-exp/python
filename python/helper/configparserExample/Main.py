from configparserExample.ConfigReader import ConfigReader

if __name__ == "__main__":
    configReader = ConfigReader()
    print(configReader.get_config_by_key("SectionTwo", "FavoriteColor", "Test"))
