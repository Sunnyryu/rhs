import pymysql
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
sys.path.append(grandparentdir)
from config.DatabaseConfig import * # DB 접속 정보 불러오기

db = None

try:
    db = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    db=DB_NAME,
    charset='utf8mb4'
    )
    sql = '''
    CREATE TABLE IF NOT EXISTS `chatbot_train_data` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `intent` VARCHAR(45) NULL,
    `ner` VARCHAR(1024) NULL,
    `query` TEXT NULL,
    `answer` TEXT NOT NULL,
    `answer_image` VARCHAR(2048) NULL,
    PRIMARY KEY (`id`))
    ENGINE = InnoDB DEFAULT CHARSET=utf8mb4
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
