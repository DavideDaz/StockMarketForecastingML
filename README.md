# Stock Market Analysis: EPS, EPS Surprise and Price Return Forecasting
Earning per Share (**EPS**) is an indicator of a company's profitability. It indicates how much money a company makes for each share of its stock and is a widely used metric for corporate profits. Investors are likely to pay more for stocks related to high EPS as it indicates a higher value of a particular company that can translates to a more profitable future return. 
Financial analysts widely use this indicator to assess the potential of a particular stock and try to estimate future earnings based on the financial statement, the income statement, balance sheet, and cash flow statement released on a quarterly base by each company. 

In general, the earnings can affect a stock in two ways. The first is its instrinsic value that indicates a possible profitability for the investors that therefore are willing to pay more for those shares. The second has an immediate effect soon after the disclosure of the real earnings value at each quarter. Indeed, in the case a company overferforms the **analysts estimate**, the price is more likely to increase as it reflects a bigger potential for the investor's return. This last case is defined as **Earning Surprise** and represents an additional indicator for the stock analysis. On the other side, a company underperforming the general analysts expectation generates a drop in the stock price.
It is therefore clear that predicting both EPS and Earning surprise can be a valuable tool for traders and investors in order to assess and forecast the profitability of a particular stock.

 Machine Learning in the last decade has proven to be a powerful tool for **time series forecasting** that in many cases has been able to overperform the traditional linear based methods widely used in the financial industry. In particular, **Recurrent Neural Networs** and variuos flavors of **LSTM** based models have produced encouraging results despite the high volatility that characterizes the Stock Market.
 This project intends to explore the potential of state of the art LSTM models to forecast EPS, EPS surprise and Return on a quarter base for different stock in the US market and possibly give some insights about how these indicators can really affect the Price trend.

 ## Data and Data Pipeline

 Here is the Description of used data and Data Pipeline