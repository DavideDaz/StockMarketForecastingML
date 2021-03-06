from datetime import datetime
from concurrent import futures
import pandas as pd
from pandas import DataFrame
import pandas_datareader.data as web
import os

def download_stock(stock):
	try:
		print(stock)
		stock_df = web.DataReader(stock,'yahoo', start_time, now_time)
		stock_df['Name'] = stock
		output_name = stock + '_prices.csv'
		stock_df.to_csv('/Users/davideconcu/Documents/Stock Analysis/DataPipeline/SPpricesYahooFinance/Stocks/' + output_name)
	except:
		bad_names.append(stock)
		print('bad: %s' % (stock))

if __name__ == '__main__':
	errorFix = True
	symbolsFile = '/Users/davideconcu/Documents/Stock Analysis/DataPipeline/WebScrapingZacks/docs/Symbols.csv'
	stockFolder = '/Stocks/'
	root = '/Users/davideconcu/Documents/Stock Analysis/DataPipeline/SPpricesYahooFinance'

	if not os.path.exists(root + stockFolder):
		os.mkdir(root + stockFolder)

	""" set the download window """
	now_time = datetime.now()
	start_time = datetime(1980, 1 , 1)

	""" list of s_anp_p companies """
	symbols = pd.read_csv(symbolsFile)
	s_and_p = list(symbols['Symbol'])
	bad_names =[] #to keep track of failed queries

	"""here we use the concurrent.futures module's ThreadPoolExecutor
		to speed up the downloads buy doing them in parallel 
		as opposed to sequentially """

	#set the maximum thread number
	max_workers = 50
	if not errorFix:
		workers = min(max_workers, len(s_and_p)) #in case a smaller number of stocks than threads was passed in
		with futures.ThreadPoolExecutor(workers) as executor:
			res = executor.map(download_stock, s_and_p)

		""" Save failed queries to a text file to retry """
		if len(bad_names) > 0:
			with open(root +'/failed_queries.txt','w') as outfile:
				for name in bad_names:
					outfile.write(name+'\n')
	else:
		errorfile = root +'/failed_queries.txt'
		errorFile = open(errorfile, "r")
		s_and_p = errorFile.readlines()
		for s in s_and_p:
			s = s.strip()
			download_stock(s)
			p = root + stockFolder + '{}_prices.csv'.format(s)
			if os.path.exists(p):
				with open(errorfile, "r") as f:
					lines = f.readlines()
				with open(errorfile, "w") as f:
					for line in lines:
						if line.strip("\n") != s:
							f.write(line) 

	