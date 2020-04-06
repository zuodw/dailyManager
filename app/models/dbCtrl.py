import pyodbc

DRIVER = '{Microsoft Access Driver (*.mdb, *.accdb)}'
PASSWORD = r'ba7fa3c49bd914f16'
DB_FILE = r'D:\code\python\dailyManager\hmi.accdb'

CONN = 'DRIVER=%s;PWD=%s;DBQ=%s' % (DRIVER, PASSWORD, DB_FILE)
print(CONN)


class DBCtrl(object):
    def dbConn(self):
        conn = pyodbc.connect(CONN)
        cur = conn.cursor()
        for table_info in cur.tables(tableType='TABLE'):
            print(table_info.table_name)
            print(cur.execute('SELECT * FROM %s' % (table_info.table_name)).fetchall())
            print('================================================')