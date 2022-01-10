year = int(input())
if year % 4 == 0:
    print("leap year")
elif year % 100 != 0:
    print("is not leap year")
elif year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")
