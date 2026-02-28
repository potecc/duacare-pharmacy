import os

class Config:
    # MySQL connection via environment variable (production) or local fallback
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', "mysql+pymysql://root:@localhost/care_db")
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/care_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')