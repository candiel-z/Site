import sqlite3

from config.config import Config


class Database(object):
    def __init__(self):
        """"""
        

        #if Config.DEBUG:
        #    self._execute(Config.DATABASE['DROP_CLIENTS'])
        #    self._execute(Config.DATABASE['DROP_ORDERS'])

        self._execute(Config.DATABASE['CREATE_CLIENTS'])
        self._execute(Config.DATABASE['CREATE_ORDERS'])

    def add(self, data) -> None:
        """"""
        
        order_id = data.get('order_id')
        first_name = data.get('first_name')
        second_name = data.get('second_name')
        mobile_number = data.get('mobile_number')

        product_names = data.getlist('product_name')
        product_amounts = data.getlist('product_amount')

        self._execute(f"""
                insert into Clients
                (order_id, first_name, second_name, mobile_number)
                values
                ('{order_id}','{first_name}','{second_name}','{mobile_number}')
        """)

        for i in range(len(product_names)):
            self._execute(f"""
                insert into Orders
                (order_id, product_name, product_amount)
                values
                ('{order_id}','{product_names[i]}','{product_amounts[i]}')
            """)

    def get_all(self):
        """"""
        
        return [self._execute("select * from Clients", read=True),
                self._execute("select * from Orders", read=True)]

    def get(self, order_id):
        """"""

        return [self._execute(f"select * from Clients where order_id='{order_id}';", read=True)[0], 
                self._execute(f"select * from Orders where order_id='{order_id}';", read=True)]


    def _execute(self, query: str, read: bool = False):
        """"""

        connection, cursor = self._connect()
        try:
            cursor.execute(query)
            if read:
                data = cursor.fetchall()
                return data
        except sqlite3.Error as e:
            print('Database._execute | ', e)
        finally:
            connection.commit()
            connection.close()

    def _connect(self):
            """"""

            try:
                connection = sqlite3.connect(Config.DATABASE['PATH'])
                cursor = connection.cursor()
            except sqlite3.Error as e:
                print('Database._connect | ', e)
                connection.close()
            else:
                return connection, cursor
