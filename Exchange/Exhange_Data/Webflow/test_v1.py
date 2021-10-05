from csv import writer
from csv import reader
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from price_catcher_1min import functCaller
    
print(functCaller())
def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)


def test_funct():
    date = datetime.now()
    print (date.strftime("%Y-%m-%d-%H:%M:%S"),date.ctime())
    data = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/Crypto Price 24h.csv'
    input_file = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/input.csv'
    output = '/Users/EL-_-KDS/Documents/website Projects/Cryptonel/Exchange/Exhange_Data/Webflow/input copy.csv'
    test_list = []

    test_list.append(date.strftime('%Y-%m-%d-%H:%M:%S'))

    with open (data, 'r') as test_file:
        csv_Reader = reader(test_file)
        next(test_file)
        for line in test_file:
            line2 = line.split(',')
            test_list.append(line2[1].replace('\n',''))
    print(len(test_list))
    add_column_in_csv(input_file, output, lambda row, line_num: row.append(test_list[line_num-1]))

    with open(output, 'r') as read_obj, \
            open(input_file, 'w', newline='') as write_obj:
            # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        for line in csv_reader:
            csv_writer.writerow(line) 


""" sched = BlockingScheduler()
# Schedule job_function to be called every two hours

sched.add_job(test_funct, 'interval', seconds=10, start_date='2021-08-15 00:00:00')
sched.start() """
