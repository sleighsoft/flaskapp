class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SECRET_KEY = None


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
