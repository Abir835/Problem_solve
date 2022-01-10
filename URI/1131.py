count = 0
Inter = 0
Gremio = 0
Empates = 0
while True:
    x, y = list(map(int, input().split()))
    count = count + 1
    print("Novo grenal (1-sim 2-nao)")

    if x > y:
        Inter = Inter+1
    elif x < y:
        Gremio = Gremio+1
    elif x == y:
        Empates = Empates+1

    n = int(input())
    if n == 1:
        continue
    if n == 2:
        break

print('{} grenais'.format(count))
print('Inter:{}'.format(Inter))
print('Gremio:{}'.format(Gremio))
print('Empates:{}'.format(Empates))

if Inter > Gremio:
    print("Inter venceu mais")
elif Inter < Gremio:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")




