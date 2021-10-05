from datetime import datetime, timedelta
import dateutil.parser
from dateutil import parser
import pandas as pd
import csv
from dateutil.relativedelta import relativedelta


date = datetime.now()
data_time = dateutil.parser.parse('2021-08-19-16:10:30')
data_time2 = dateutil.parser.parse('2021-08-19-16:09:30')
then = timedelta()
test_date = data_time - data_time2

test = [1,2,3,7,5,4,9,6,8]
test.sort()
print(test)

