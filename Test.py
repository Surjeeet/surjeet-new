a = int(input("Enter the month in numerical form :"))
if(a>12 or a<0):
  print("Error: Invalid Month Input")
  exit(1)
b = int(input("Enter the day in numeric form :"))
if (b>31 or b<0):
  print("Error: Invalid Day Input")
  exit(1)
c =int(input("Enter the year as two numerical digits :"))
if (c>99 or c<0):
  print("Error: Invalid Year Input")
  exit(1)
else:
  print( a, "/", b, "/", c)
  print("Success: Congratulations! you entered the correct date.")