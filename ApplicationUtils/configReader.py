from configparser import ConfigParser

def readConfig(section, key):
    config = ConfigParser()
    config.read("..//DataConfiguration//conf.ini")
    #config.read("..//DataConfiguration//conf.ini")
    return (config.get(section, key))