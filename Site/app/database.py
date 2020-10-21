import sqlite3

from config.config import Config


class Database(object):
    def __init__(self):
        """"""
        

        if Config.DEBUG:
            self._execute("""
                drop table if exists Orders
            """)

        self._execute("""
            create table if not exists Orders (
                id integer primary key,
                name text not null,
                surname text not null,
                mobile_number text not null unique
            );
        """)

    def _connect(self):
            """"""

            try:
                connection = sqlite3.connect(Config.DATABASE)
                cursor = connection.cursor()
            except sqlite3.Error as e:
                print('database._connect |', e)
                connection.close()
            else:
                return connection, cursor

    def add(self, name: str, surname: str, mobile_number: str) -> None:
        """"""
        
        self._execute(f"""
                insert into Orders
                (name, surname, mobile_number)
                values
                ('{name}','{surname}','{mobile_number}')
        """)

    def get(self):
        """"""
        
        return self._execute("""select * from Orders""", read=True)

    def _execute(self, query: str, read: bool = False):
        """"""

        connection, cursor = self._connect()
        try:
            cursor.execute(query)
            if read:
                data = cursor.fetchall()
                return data
        except sqlite3.Error as e:
            print('Database._execute |', e)
        finally:
            connection.commit()
            connection.close()
