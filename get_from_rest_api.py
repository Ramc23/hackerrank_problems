#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json
import datetime



#
# Complete the 'numDevices' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER threshold
#  3. STRING dateStr
#

def numDevices(statusQuery, threshold, dateStr):
    # Write your code here
    b_url = 'https://jsonmock.hackerrank.com/api/iot_devices/search?status=' 
    page =1
    total_pages =1
    count =0
    
    while page <= total_pages:
        url = b_url + str(statusQuery) + "&page=" + str(page)
        apirequest = requests.get(url)
        result = apirequest.json()
        
        if page == 1:
            total_pages = result['total_pages']
            #print(total_pages)
         
        events = result['data']
        
        for event in events:
            root_ther = event["operatingParams"]["rootThreshold"]
            if event["timestamp"] :
                millis = int(event["timestamp"]  )
                date_time = datetime.datetime.fromtimestamp(millis/1000.0)
                date = str(date_time).split("-", 2)
                to_match = date[1] + "-" + date[0]
                
                if root_ther > threshold and dateStr == to_match:
                    print("root thersold : " + str(root_ther))
                    print("timestamp : " + str(to_match))
                    count= count+ 1
         
        
        page+=1
    print(" count " + str(count))
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    statusQuery = input()

    threshold = int(input().strip())

    dateStr = input()

    result = numDevices(statusQuery, threshold, dateStr)

    fptr.write(str(result) + '\n')

    fptr.close()
