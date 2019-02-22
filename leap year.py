year=2019
if(year%4)==0:
   if(year%100)==0:
      if(year%400)==0:
         print("the year is leap year",year)
      else:
         print("the year is not",year)
   else:
     print("the year is leap year")
else:
   print("the year is not leap year")
   
