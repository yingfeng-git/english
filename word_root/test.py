from word_root import connect_mysql
import sys


def test_read_data():
    sql = connect_mysql.ConnectMysql()
    p = sql.connect()
    p.execute("select * from eng_word limit 10;")
    data = p.fetchall()
    print(data)


