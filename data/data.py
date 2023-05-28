import sqlite3 as sq


class Database(object):

    def __init__(self, path):
        self.connection = sq.connect(path)
        self.connection.execute('pragma foreign_keys = on')
        self.connection.commit()
        self.cur = self.connection.cursor()

    def create_tables(self):
        self.query(
            'CREATE TABLE IF NOT EXISTS users (id int, visa text, ariza_shakli text, davlat text,'
            'shahar text, visametric text, turlari text, soni int, name text, firstname text,'
            'mileti text, birthday int, month int, year int, number_passport text,'
            'year_passport text, phone_number text, alt_phone text, email text,'
            'password text)')

    def query(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.connection.commit()

    def fetchone(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()

    def __del__(self):
        self.connection.close()