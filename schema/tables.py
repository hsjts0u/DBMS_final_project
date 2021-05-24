tables = (
    """
    CREATE TABLE earning_data(
    ticker varchar(20),
    year int,
    earning bigint,
    primary key (ticker,year)
    )
    """,
    """
    CREATE TABLE revenue_data(
    ticker varchar(20),
    year int,
    revenue bigint,
    primary key (ticker,year)
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
    primary key (ticker, date)
    )
    """,
    """
    CREATE TABLE history_stock_data(
    ticker varchar(20),
    day date,
    open float,
    high float,
    low float,
    close float,
    volume bigint,
    primary key (ticker, day)
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
