'''
Created on 26 Sep 2019

@author: Aruna
'''

import sys
import unittest
import io


import ParseCSV

class TestParseCSV(unittest.TestCase):
    def test_sortbyrent(self):
        Output = io.StringIO()
        sys.stdout = Output
        parser = ParseCSV.ParseCSV('Mobile Phone Masts.csv')
        parser.sortbyrent()
        sys.stdout = sys.__stdout__
        self.assertRegex(Output.getvalue(),'produce a list sorted by Current Rent')
        
          
    def test_leaseyearfilter(self):
        Output = io.StringIO()
        sys.stdout = Output
        parser = ParseCSV.ParseCSV('Mobile Phone Masts.csv')
        parser.leaseyearfilter()
        sys.stdout = sys.__stdout__
        self.assertRegex(Output.getvalue(),'From the list of all mast data create new list of mast data with Lease Years = 25')
        
    
    def test_cntofmasts(self):
        Output = io.StringIO()
        sys.stdout = Output
        parser = ParseCSV.ParseCSV('Mobile Phone Masts.csv')
        parser.cntofmasts()
        sys.stdout = sys.__stdout__
        self.assertRegex(Output.getvalue(),'Create a dictionary containing tenant name')
        
    def test_leasestartfilter(self):
        Output = io.StringIO()
        sys.stdout = Output
        parser = ParseCSV.ParseCSV('Mobile Phone Masts.csv')
        parser.leasestartfilter()
        sys.stdout = sys.__stdout__
        self.assertRegex(Output.getvalue(),'List the data for rentals with Lease Start Date between')  
        
    def test_filenotfound(self):
        Output = io.StringIO()
        sys.stdout = Output
        parser = ParseCSV.ParseCSV('Mobile Phone Masts junk.csv')
        sys.stdout = sys.__stdout__
        self.assertRegex(Output.getvalue(),'File does not exist')
        
        
if __name__ == '__main__':
    unittest.main()