# ParseCSV
Parse a given file and filter the data according to the requirements and display according to the requirements



Instructions to run:

1) To run the code directly:
- python ParseCSV.py
- choose the feature from the listed options

2) To run the tests:

- python test_ParseCSV.py

3) Mobile Phone Masts.csv used will be present in the same directory when cloned


Documentation:

Code:

The main class ParseCSV is present in ParseCSV.py module and the code is self explanatory. This class has 4 methods corresponsing to the 4 requirements given in the test question.
 The constructor of the class parses the given file and generates a list of lists (self.sortedlist) which is a class attribute which can then be used by other methods belonging to the class.
 
 The module also contains the main method so it can be run independently
 
 Tests:
 
 Currently basic tests are added for each method (requirement) to make sure the methods are doing what they are supposed to do.
 unittest module has been used for running tests. 
 
 The data file has been downloaded from https://data.gov.uk/dataset/mobile-phone-masts as suggested.


