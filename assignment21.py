
'''
Created on Sep 24, 2018

@author: jatin.pal
'''
def generate_next_date(day,month,year):
    if month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10:
        if day==31:
            next_day=1
            next_month=month+1
            next_year=year
        else:
            next_day=day+1
            next_month=month
            next_year=year
    elif month in [4,6,9,11]:
        if day== 31:
            next_day=1
            next_month=month+1
            next_year=year
        else:
            next_day=day+1
            next_month=month
            next_year=year
    elif month==2  :
        if ((year%4==0 and year%100!=0) or year%400==0):
            if day == 29:
                next_day=1 
                next_month=month+1 
                next_year=year
            else:
                next_day=day+1 
                next_month=month
                next_year=year
        else:
            if day == 28:
                next_day=1 
                next_month=month+1 
                next_year=year
            else:
                next_day=day+1 
                next_month=month
                next_year=year
    else:
        if day == 31:
            next_day=1 
            next_month=1 
            next_year=year+1
        else:
            next_day=day+1 
            next_month=month
            next_year=year        
    #Start writing your code here

    print(next_day,"-",next_month,"-",next_year)


generate_next_date(28,2,1800)