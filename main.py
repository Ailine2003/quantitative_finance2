import pandas as pd
import numpy as np
from modules.financial_functions import portfolio_volatility, portfolio_returns, VaR
from modules.backend import tickers_by_issuer

if _name_ =='_main_': 
    #Obtener tickers de ishares
    tickers = tickers_by_issuer(issuer= 'iShares')
    list_tickers = list(tickers['TICKER'])
    
    for ticker in list_tickers:
        print(f'Instrumento: {ticker}')
    
    #Portafolio de renta fija
    tickers_rf = tickers[tickers['CATEGORIA']=='ETF RF']
    list_tickers_rf = list(tickers_rf['TICKER'])