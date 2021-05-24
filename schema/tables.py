tables = (
    """
    CREATE TABLE earning_data(
    ticker varchar(20),
    2017revenue int,
    2018revenue int,
    2019revenue int,
    2020revenue int,
    2017earning int,
    2018earning int,
    2019earning int,
    2020earning int,
    primary key (ticker)
    )
    """,
    """
    CREATE TABLE financial(
    ticker varchar(20) NOT NULL,
    date date,
    research_development bigint,
    net_income bigint,
    gross_profit bigint,
    ebit bigint,
    operating_income bigint,
    biginterest_expense bigint,
    primary key (ticker)
    )
    """,
    """
    CREATE TABLE history_stock_data(
    id int,
    ticker varchar(20),
    day date,
    open float,
    high float,
    low float,
    close float,
    adj_close float,
    volume int,
    primary key (id)
    )
    """,
    """
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
    primary key (ticker)
    )
    """,
    """
    CREATE TABLE stock_list(
    ticker varchar(100),
    country varchar(100),
    primary key (ticker)
    )
    """
    )
