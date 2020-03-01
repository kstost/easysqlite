from  easysqlite import EasySQLite

con = EasySQLite()
con.query("CREATE TABLE other(word text, meaning text);")
con.query("CREATE TABLE dictionary(word text, meaning text);")
con.query('INSERT INTO dictionary VALUES(:word, :meaning);', {"word":'hello', "meaning":'안녕'})
con.query('INSERT INTO dictionary (word, meaning)VALUES(?,?);', ('apple', '사과'))
con.query('INSERT INTO dictionary (word, meaning)VALUES(?,?);', [('tiger', '호랑이'), ('sun', '태양')])
select = con.query('SELECT * FROM dictionary WHERE word=? or word=?', ('tiger','apple'))
for line in select:
    print(line)
print(con.tables())
con.close()
