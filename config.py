import os

class Config(object):
    MYSQL_DATABASE_DB = 'uranium_database'
    MYSQL_DATABASE_HOST = 'localhost'
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'Muff4hire'
    CESIUM_API_KEY='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJjMzM5MjRiOS0wYjgxLTRkYzMtYTE5Ni04OTFiMTg0MDg5YzYiLCJpZCI6NjQxNSwic2NvcGVzIjpbImFzciIsImdjIl0sImlhdCI6MTU0NjQ3ODgzMX0.Cp1Kr0kwNVv9Kpv07OafSLMAOyTJcQdKyaAxprlu4VI'

    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #FLASK_ENV=development
    DEBUG = False



# class Config(object):
#     MYSQL_DATABASE_DB = 'uranium_database'
#     MYSQL_DATABASE_HOST = 'localhost'
#     DEBUG = False
#     print('I am in config')
#
# class DevelopmentConfig(Config):
#     print('I am in development')
#     DEBUG = True
#
# class ProductionConfig(Config):
#     print('I am in production')
#     MYSQL_DATABASE_DB = 'uranium_database'
#
# app_config = {
#     'development': DevelopmentConfig,
#     'production': ProductionConfig
# }
