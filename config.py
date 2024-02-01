import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///stockmarketparty.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Flags for variable pricing and payoffs
    VARIABLE_ACTIVITY_PAYOFFS = True
    VARIABLE_DRINK_PRICES = True

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    # Testing-specific configurations
