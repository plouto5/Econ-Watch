import quandl
import time
from key import key

# Quandl US Econ data API Code
US_data_links = [            'FRED/GDP',
                        'FRED/GDPC1',
                        'FRED/CPIAUCSL',
                        'FRED/BASE',
                        'FRED/DFF',
                        'FRED/UNRATE',
                        'FRED/GFDEBTN',
                        'FRED/PSAVERT',
                        'FRED/MEHOINUSA672N',
                        'FRED/NAPM'
           ]

quandl.ApiConfig.api_key = key

for x in fx_links:
    print(x)
    df = quandl.get(x)
    df.to_csv(x[5:]+'.csv')
    time.sleep(20)
