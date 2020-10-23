drop table if exists Clients;

drop table if exists Orders;

create table if not exists Clients (
                    ididentifier integer unique,
                    first_name text not null,
                    second_name text not null,
                    mobile_number text not null unique
            );

create table if not exists Orders (
                    ididentifier integer,
                    product_name text not null,
                    product_amount integer not null
            );
