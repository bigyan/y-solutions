# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 13:59:24 2014

author: Bigyan Adhikary
email: bigyan.adhikary@gmail.com
"""

import csv
import re

ifile = open('amp-unorganised-location.csv','rU')
ofile = open('amp-organised-location.csv','wb')
reader = csv.reader(ifile)
writer = csv.writer(ofile)

rownum=1    # Used to track header. Also used for debugging purposes

for row in reader:
    if rownum==1:   # Check if line is header
        writer.writerow ( ('AMP ID','Project Title','Status','District','City') )
        rownum+=1
    else:
        for i in row[3].split('\n'):
            j = re.split('([a-zA-Z_][a-zA-Z_\s]*[a-zA-Z_])',i)
#            print rownum, j    # For debugging purposes only
            if len(j)==5:
                writer.writerow( (row[0],row[1],row[2],j[1],j[3]) )
            elif len(j)==1:
                writer.writerow( (row[0],row[1],row[2],'','') )                
            else:
                writer.writerow( (row[0],row[1],row[2],'ERROR','ERROR') )                
        rownum+=1
        
ifile.close()
ofile.close()