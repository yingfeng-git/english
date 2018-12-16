from word_root import connect_mysql as mysql

p = mysql.ConnectMysql().connect()


def sql_query(query):
    p.execute(query)
    return p.fetchall()


def eng_ch(eng):
    return sql_query(f'select * from eng_word where english like "%{eng}%";')


def ch_eng(ch):
    return sql_query(f'select * from eng_word where chinese like "%{ch}%";')


def is_chinese(uchar):
    """
    判断一个unicode是否是汉字
    """
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return True
    else:
        return False


top20000 = sql_query('select word from top20000_word where word = "asdfasfasfasdfasf" ;')
while 1:
    word = input("输入中文或者英文:")
    if is_chinese(word):
        for i in ch_eng(word):
            print(i)
    else:
        for i in eng_ch(word):
            print(i)




