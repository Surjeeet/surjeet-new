Month = int(input ("Enter the month in the numeric form."))
date = int(input ("enter date"))
year = int(input ("enter year"))
dd=1

if Month >0 and Month <=12:
    dd = 1
else:
    dd=0
    print("Error: Invalid Month Input")


if date >0 and date <=31:
    dd = 1
else:
    dd=0
    print("Error: Invalid Date Input")

if year >0 and year <=99:
    dd = 1
else:
    dd=0

if dd == 0:
    print("invalid")
else:
 print("Success: Congratulations! you entered the correct date.") 
 print("the date is",Month,"/",date,"/",year)
