year = int(input("input the year....: "))

if year % 4 == 0:
    print(year, "is Leap Year")
elif year % 100 == 0:
    print(year, "is Leap Year")
elif year % 400 == 0:
    print(year, "is Leap Year")
else:
    print(year, "is Not leap year")
