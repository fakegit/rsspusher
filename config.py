# coding:utf-8
URL = ""
TIMER = 5*60 # second
DEBUG = True
if DEBUG:
    import logging
    logger = logging.getLogger('peewee')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

# Bot
TELEGRAM_KEYS = "850313928:AAHAfmlDrHzOvWw8G21oGSfAYh0xiwNyGpM"
WEBHOOKING = URL + "/"+TELEGRAM_KEYS
YOUR_CHAT_ID_FOR_ADMIN = 103359874


# DataBase
ISMYSQL = False
MYSQL_HOST = "localhost"
MYSQL_DATABASE = "rss"
MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "root"
MYSQL_PORT = 3306
DB_PATH = "rss.db"
