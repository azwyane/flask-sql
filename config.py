from configparser import ConfigParser

import os

PATH = os.getcwd() + '/DataBase/config.ini'



def get_config(filename= PATH,section='mysql'):
    parser = ConfigParser()
    parser.read(filename)
    db_conf = {}
    if parser.has_section(section):
        key_val_list = parser.items(section)
        db_conf = dict(key_val_list)
    
    return db_conf