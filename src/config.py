class Config():
    SECRET_KEY='A98njC321s*aVF&O'
class DevelopmentConfig(Config):
    DEBUG=True
    #Database Config
    MySQL_HOST ='localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'barcodesystem'
    MYSQL_CHARSET = 'utf8'




config={
        "development":DevelopmentConfig
    }

    