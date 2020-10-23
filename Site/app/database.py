import sqlite3

from config.config import Config


class Database(object):
    def __init__(self):
        """"""
        

        if Config.DEBUG:
            self._execute('drop table if exists Clients;')
            self._execute('drop table if exists Orders;')

        self._execute("""
            create table if not exists Clients (
                    ididentifier integer unique,
                    first_name text not null,
                    second_name text not null,
                    mobile_number text not null unique
            );
        """)
        self._execute("""
            create table if not exists Orders (
                    ididentifier integer,
                    product_name text not null,
                    product_amount integer not null
            );

        """)

    def add(self, data) -> None:
        """"""
        
        ididentifier = data.get('ididentifier')
        first_name = data.get('first_name')
        second_name = data.get('second_name')
        mobile_number = data.get('mobile_number')

        product_names = data.getlist('product_name')
        product_amount = data.getlist('product_amount')

        self._execute(f"""
                insert into Clients
                (ididentifier, first_name, second_name, mobile_number)
                values
                ('{ididentifier}','{first_name}','{second_name}','{mobile_number}')
        """)
        for i in range(len(product_names)):
            self._execute(f"""
                insert into Orders
                (ididentifier, product_name, product_amount)
                values
                ('{ididentifier}','{product_names[i]}','{product_amount[i]}')
            """)

    def get(self):
        """"""
        
        return self._execute("""select * from Clients""", read=True)

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
