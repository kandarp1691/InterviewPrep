import MySQLdb

db = MySQLdb.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'Rockwell1991!',
                     db = 'test')

cursor = db.cursor()

cursor.execute('SELECT * FROM items')

for row in cursor.fetchall():
    print row

db.close()


