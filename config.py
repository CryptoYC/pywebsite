class Config:
    """
    Set Flask configuration vars from .env file.
    """
    # General
    # TESTING = True
    # FLASK_DEBUG = True
    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost/website'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
