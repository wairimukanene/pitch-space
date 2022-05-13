
import os


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wairimu:wairimu12@localhost/space'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mercykanene254@gmail.com'
    MAIL_PASSWORD = 'naivasha2020'
    
    



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    DEBUG = True
    
    

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    

   
DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}


 

  