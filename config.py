SECRET_KEY = 'thisismyfirstownblog'

username = 'root'
password = 'root'
hostname = '127.0.0.1'
port = 3306
database = 'myblog'
DB_URI = f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}?charset=utf8'
SQLALCHEMY_DATABASE_URI = DB_URI

