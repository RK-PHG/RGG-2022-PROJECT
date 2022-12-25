# 数据库连接配置

HOSTNAME = "127.0.0.1"
PORT = 3306
PASSWORD = "zju13364225501"
USERNAME = "root"
DATABASE = "cmdbs"

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

