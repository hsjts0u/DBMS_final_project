import yfinance as yf

msft = yf.Ticker("MSFT")
hist = msft.history(period="max")
print(type(msft.financials))

fin = msft.financials

for row in fin.loc["Ebit"]:
    print(row)

