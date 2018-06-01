import os
import quandl
import time
from hidden.directory import path
from hidden.key import key
from Data_Lists.US_data import *


quandl.ApiConfig.api_key = key

for x in US_data_links:
    print(x)
    df = quandl.get(x)
    df.to_csv(os.path.join(path,x[5:]+'.csv'))
    time.sleep(20)
