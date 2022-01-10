x = 0
y = 0
z = 0
while True:
    a = int(input())
    if a == 4:
        break
    else:
        if a == 1:
            x = x+1
        elif a == 2:
            y = y+1
        elif a == 3:
            z = z+1
        else:
            continue
print("MUITO OBRIGADO")
print("Alcool:",x)
print("Gasolina:",y)
print("Diesel:",z)