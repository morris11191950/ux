class Config(object):
    MYSQL_DATABASE_DB = 'uranium_database'
    MYSQL_DATABASE_HOST = 'localhost'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    MYSQL_DATABASE_DB = 'uranium_database'

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
