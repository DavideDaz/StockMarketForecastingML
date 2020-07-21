# StockMarketForecastingML
Stock Market  prices forecasting with Machine Learning methods based on Fundamentals and Technical analysis

## Data Web Scraping from Zacks.com

All the historical data are collected from Zacks.com. There is not a free of charge API available to quickcly retreive the historical tables, therefore we built a framework on Python and Selenium to amutomatically dowload the main fundamentals for the S&P 500 tickers.

### mainScraping.py

This file allows three kind of data scraping from Zacks.com:

* **performEpsScraping**: if set to *True*, performs the scraping of the EPS suprise data for the symbols listed in */docs/Symbols.csv* and saves a .csv table for each ticker in *epsHistorical* directory. In the case the table is not available in Zacks.com or an error has been raised during the Scraping, the symbol is added to the Error list in */docs/failed_queries_EPS.txt*.

* **performFundamentalsScraping**: if set to *True*, performs the scraping of the fundamentals data listed in */docs/FundamnetalsList.csv* for the symbols listed in *docs/Symbols.csv* and saves a *.csv* table for each fundamnetal of each ticker in *FundamentalsHistorical/'symbol'/* directory. In the case the table is not available in Zacks.com or an error has been raised during the Scraping, the symbol is added to the Error list in */docs/failed_queries_fundamentals.txt*.

* **ErrorFix**: if set to *True*, will read the  */docs/failed_queries_fundamentals.txt* generated by the previous fundamentals scraping and re-try a second attempt to retreive the missing tables listed. Is recommended to use this function alone and disable the previous two in order to follow a logic error fixing, as in the following example:

'''

	performEpsScraping = False
   	performFundamentalsScraping = False
	errorFix = True



Note that this function is only available for the fundamentals table and not for the EPS ones, as in this latest an additional attemp can be made allowing the Eps scraping and adding a new line specifiyng the symbols which we want to re-try with as the following example with AAPL, GOOG and AMX:



    tickersData = pd.read_csv(wd+'/docs/Symbols.csv')
    tickers = list(tickersData['Symbol'])
    sector = list(tickersData['GICS Sector'])

    tickers = ['AAPL','GOOG','AMX']
    zScraping = ZacksWebScraping.tabScrap()
    

**Final Note**: Given the large amount of times needed to scrap the Fundamentals for each symbol, the scraping process can be divided into smaller chuncks of Symbols by specifing them from the tickers list (Usually 10 tickers take around 2 hours). See this example to retreive the Fundamentals of the tickers included in the chunk *[250:270]* by adding a line to the file:



    tickers = list(tickersData['Symbol'])
    sector = list(tickersData['GICS Sector'])

    tickers = tickers[250:270]

    zScraping = ZacksWebScraping.tabScrap()
  
