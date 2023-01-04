import os
class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

    ASSETS_ROOT=os.getenv("ASSETS_ROOT","/static")

class ProductionConfig(Config):
 
   
    # Securidad
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # database



class DebugConfig(Config):
    DEBUG = True # Modo desarrollador True o En hosting False

config_dict={
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}