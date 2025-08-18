'''
3 for months 12
6 for months 12.5
1 year 13
3 year 14
5 for year 15
5 or above
'''
def intrest(cash,duration,month_Or_year):
    intrest_3_month=0.12
    intrest_6_month=0.125
    intrest_1_year=0.13
    intrest_3_year=0.14
    intrest_5_year=0.15
    intrest_5_year_over=0.15
    if month_Or_year=="month":
        if duration==3:
            cash=cash+cash*intrest_3_month*(3/12)
        elif duration==6:
            cash=cash+cash*intrest_6_month*(6/12)
     if month_Or_year=="year":
        if duration==1:
            cash=cash+cash*intrest_1_year
        elif duration==3:
            cash=cash+cash*intrest_3_year
        elif duration==5:
            cash=cash+cash*intrest_5_year
        elif duration>5:
            cash=cash+cash*intrest_5_year_over
            
    print(cash)

intrest(100000,1,'year')