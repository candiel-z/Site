class Config(object):
    DEBUG = True
    DATABASE = {
        'PATH': r'database.db',
        'DROP_CLIENTS': 'drop table if exists Clients;',
        'DROP_ORDERS': 'drop table if exists Orders;',
        'CREATE_CLIENTS': '''
            create table if not exists Clients (
                    order_id integer unique,
                    first_name text not null,
                    second_name text not null,
                    mobile_number text not null unique
            );''',
        'CREATE_ORDERS': '''
            create table if not exists Orders (
                    order_id integer,
                    product_name text not null,
                    product_amount integer not null
            );''',
    }
