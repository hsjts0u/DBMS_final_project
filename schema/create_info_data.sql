CREATE TABLE info_data(
    ticker varchar(20),
    dividendRate float,
    beta float,
    52WeekChange float,
    shortName varchar(100),
    longName varchar(100),
    forwardEps float,
    bookValue float,
    priceToBook float,
    shortRatio float,
	longBusinessSummary varchar(1000),
	logo_url varchar(1000),
    primary key (ticker)
);



