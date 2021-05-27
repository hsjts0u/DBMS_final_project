CREATE TABLE stock_list(
    ticker varchar(100),
    name varchar(100),
    exchange varchar(20),
    category_name varchar(100),
    country varchar(50)
    primary key (ticker, exchange)
);

load data local infile './stock_csv_list.csv'
into table stock_list
fields terminated by ','
lines terminated by '\n'
ignore 1 lines;







