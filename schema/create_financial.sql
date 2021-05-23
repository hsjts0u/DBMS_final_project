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
);
