'''
Created on 26 Sep 2019

@author: Aruna
'''

import os
import sys
import csv
import operator
from datetime import datetime


class ParseCSV:
    def __init__(self,fname):
        self.sortedlist = None
        
        if not os.path.exists(fname):
            print('File does not exist')
        with open(fname) as reader:
            csvobj = csv.reader(reader)
            self.sortedlist = sorted(csvobj,key=operator.itemgetter(10))
            del self.sortedlist[-1]
            
    def sortbyrent(self):
        print('\n\n1: produce a list sorted by Current Rent in ascending order. Obtain the first 5 items from the resultant list and  output to the console\n')
        for i in range(5):
            print(self.sortedlist[i])
          
        
    def leaseyearfilter(self):
        print('\n\n2: From the list of all mast data create new list of mast data with Lease Years = 25 years\n')
        
        list2 = [a for a in self.sortedlist if int(a[9]) == 25]
        for lst in list2:
            #Total rent is 25 multiplied by current rent as it is assumed that current is annual
            totalrent = 25*int(lst[-1].split('.')[0])
            print (lst)
            print('Total rent : {}'.format(totalrent))
            
    def cntofmasts(self):
        print('\n\n3: Create a dictionary containing tenant name and a count of masts for each tenant. Output the dictionary to the console in a readable form\n')
        dic = {}
        print('Tenant name|Count of masts\n')
        for lst in self.sortedlist:
            if lst[6] not in dic:
                dic[lst[6]] = 1
            else:
                dic[lst[6]] += 1
                
        for key,val in dic.items():
            print(key,'|',val)
    
    def leasestartfilter(self):
        print('\n\n4: List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007\n')
        
        startend = [v for v in self.sortedlist if datetime.strptime('1/Jun/1999', '%d/%b/%Y') < datetime.strptime(v[7], '%d %b %Y') < datetime.strptime('31/Aug/2007', '%d/%b/%Y')]
        for lst in startend:
            lst[-3] = datetime.strptime(lst[-3], '%d %b %Y').strftime('%d/%m/%Y')
            lst[-4] = datetime.strptime(lst[-4], '%d %b %Y').strftime('%d/%m/%Y')
            print (lst)
            
    
    
if __name__ == '__main__':
    ParseCSVobj = ParseCSV('Mobile Phone Masts.csv')
    if ParseCSVobj.sortedlist is None:
        sys.exit()
    print ('''Enter the filter/display option:
    1: produce a list sorted by Current Rent in ascending order. Obtain the first 5 items from the resultant list and  output to the console')
    2: From the list of all mast data create new list of mast data with Lease Years = 25 years
    3: Create a dictionary containing tenant name and a count of masts for each tenant. Output the dictionary to the console in a readable form.
    4: List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007
    5: All the Above''')
    Opt = input()
    if Opt not in ['1','2','3','4','5']:
        print('Option entered is invalid.')
    if Opt in ['1', '5']:
        ParseCSVobj.sortbyrent()
    if Opt in ['2', '5']:
        ParseCSVobj.leaseyearfilter()
    if Opt in ['3', '5']:
        ParseCSVobj.cntofmasts()
    if Opt in ['4', '5']:
        ParseCSVobj.leasestartfilter()