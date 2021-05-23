CREATE TABLE financial(
    ticker varchar(20) NOT NULL,
    date date,
    research_development int,
    net_income int,
    gross_profit int,
    ebit int,
    operating_income int,
    interest_expense int,
    primary key (ticker)
);
