import os
from dotenv import load_dotenv

class Config(object):
    load_dotenv(verbose=True)
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    LOG_PATH = os.path.abspath(APP_DIR)+"/log"

    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    
    load_dotenv(verbose=True, dotenv_path=ROOT_DIR+"/confs/database/mysql/.env")
    MYSQL_DATABASE_USERNAME = os.getenv("MYSQL_DATABASE_USERNAME")
    MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
    MYSQL_DATABASE_HOST = os.getenv("MYSQL_DATABASE_HOST")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}:{DB_PORT}/{DB_NAME}?charset=utf8"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.format(DB_USER=MYSQL_DATABASE_USERNAME,
                                                             DB_PASS=MYSQL_ROOT_PASSWORD,
                                                             DB_ADDR=MYSQL_DATABASE_HOST,
                                                             DB_PORT=MYSQL_PORT,
                                                             DB_NAME=MYSQL_DATABASE)
    
class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)