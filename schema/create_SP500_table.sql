CREATE TABLE SP500_stock_data(
    ticker varchar(20),
    day date,
    open float,
    high float,
    low float,
    close float,
    volume bigint,
    primary key (ticker, day)
);





