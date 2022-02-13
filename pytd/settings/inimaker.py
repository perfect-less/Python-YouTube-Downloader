import configparser
import os, sys



def CreateConfigFile():

    this_dir = os.path.dirname( os.path.abspath(__file__) )
    config_path = os.path.join(this_dir, 'pytdconfig.ini')

    if not os.path.exists(config_path):
        pass
        
        # Create the ini config



