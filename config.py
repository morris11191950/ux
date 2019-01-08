class Config(object):
    MYSQL_DATABASE_DB = 'uranium_database'
    MYSQL_DATABASE_HOST = 'localhost'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
