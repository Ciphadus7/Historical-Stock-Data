import requests
from datetime import datetime
import time

print("Enter the ticker symbol(stock symbol): ")
print("Don't know the ticker symbol? I gotchu - (https://finance.yahoo.com/lookup/)")
ticker = input("--> ")
from_date = input('Enter start date in yyyy/mm/dd format: ')
to_date = input('Enter end date in yyyy/mm/dd format: ')


from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


url =(f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true")


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} #Should run with chrome, safari and mozilla.

content = requests.get(url, headers=headers).content
print(content)

with open('data.csv', 'wb') as f:           #write the data to a .csv file
    f.write(content)

print('---------------------------')
print("Data has been saved to 'data.csv' in your current directory.")

###Codes done. If you wanna change a few things, go ahead.