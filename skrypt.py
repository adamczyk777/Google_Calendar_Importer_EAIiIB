import json
import csv
from pprint import pprint

# Importing data from JSON FILE
with open('plan.json',  encoding='utf-8') as data_file:
    data = json.load(data_file)
"""
# Exporting to CSV
with open('csvfile.csv','w', 'utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    RESULT = ['CHUJ', 'DUPA', 'CYCKI']
    
    for record in data:
        writer.writerow(RESULT)
    
    
    
    
    """
HEADER = ['Subject', 'Start Date', 'Start Time',
          'End Date', 'End Time', 'Description']
with open("output.csv", 'w', encoding='utf-8', newline='') as resultFile:
    wr = csv.writer(resultFile, delimiter=',', quoting=csv.QUOTE_ALL)
    wr.writerow(HEADER)
    RESULT = []
    valid_groups = [0, 1.1]
    for record in data:
        if record['group'] in valid_groups:
            title_data = record['title'].split(',')
            title = title_data[0]
            if title == 'Język obcy':
                continue
            description = ' '.join(title_data[1:]).replace('<br/>', ' ')
            start_date = record['start'].split('T')[0].replace('-', '/')
            start_time = record['start'].split('T')[1][:5]
            end_date = record['end'].split('T')[0].replace('-', '/')
            end_time = record['end'].split('T')[1][:5]
            RESULT = [title, start_date, start_time,
                      end_date, end_time, description]
            # print(RESULT)
            wr.writerow(RESULT)
            # print(record['title'].split(','))
