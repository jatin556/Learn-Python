#PF-Assgn-22
'''
Created on Sep 18, 2018

@author: jatin.pal
'''
def find_leap_years(given_year):
    for given_year in range(given_year,given_year+61):
        if((given_year%4==0 and given_year%100!=0) or given_year%400==0):
            print(given_year)
find_leap_years(1784)            