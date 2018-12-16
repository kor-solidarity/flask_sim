import os
SECRET_KEY = 'secret_here'
DEBUG = True

DB_USERNAME = 'username'
DB_PASSWORD = "pass"
BLOG_DB_NAME = 'dbname'
DB_HOST = os.getenv('IP', 'ip')
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
