def days_in_month(y, m):
    days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if ((y%4==0 and y%100!=0 )or y%400==0) and m==2:
        return 29
    else:
        return days_list[m-1]
year=int(input("Enter the year"))
month=int(input("Enter the month as the number"))
answer=days_in_month(year,month)
print("number of days is", answer)
