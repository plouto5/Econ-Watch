import os
import quandl
import time
from directory import path
from key import key
from US_data import *


quandl.ApiConfig.api_key = key

for x in US_data_links:
    print(x)
    df = quandl.get(x)
    df.to_csv(os.path.join(path,x[5:]+'.csv'))
    time.sleep(20)
