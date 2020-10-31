from configparser import ConfigParser
import os

# The path neeeds to be changed accordingly 
# based on the location of the config.ini
# Config.ini is the editable cofig file for the database

PATH = os.getcwd() + '/DataBase/config.ini'


def get_config(filename= PATH,section='mysql'):
    parser = ConfigParser()
    parser.read(filename)
    db_conf = {}
    if parser.has_section(section):
        key_val_list = parser.items(section)
        db_conf = dict(key_val_list)
    
    return db_conf