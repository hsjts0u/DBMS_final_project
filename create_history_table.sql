create table history_stock_data(
    ticker int,
    day date,
    open float,
    high float,
    low float,
    close float,
    adj close float,
    volume int,
    primary key (stock_id, date)
);





