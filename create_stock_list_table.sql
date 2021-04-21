create table stock_list(
    ticker varchar(100),
    country varchar(100),
    primary key (ticker)
);

load data local infile './stock_csv_list.csv'
into table stock_list
fields terminated by ','
lines terminated by '\n'
ignore 1 lines;







