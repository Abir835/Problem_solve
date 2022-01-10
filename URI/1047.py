a, b, c, d = list(map(int, input().split()))
e = (a * 60) + b
f = (c * 60) + d
dif = f - e
if dif <= 0:
    dif += 24 * 60
time = dif // 60
m = dif % 60
print(f"O JOGO DUROU {time} HORA(S) E {m} MINUTO(S)")
