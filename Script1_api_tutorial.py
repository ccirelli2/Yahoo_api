# PURPOSE:  BASIC FUNCTIONS OF API


# Import Library
from yahoofinancials import YahooFinancials 

# Create a yahoo_finance object for a specific company
ticker = 'AAPL'
yahoo_financials = YahooFinancials(ticker)

balance_sheet_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')
print(balance_sheet_data_qt)



