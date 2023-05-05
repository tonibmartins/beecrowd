pos = 0
soma = 0

for i in range(6):
    x = float(input())
    if (x > 0):
        pos += 1
        soma += x

media = soma / pos
print(pos, 'valores positivos')
print('%.1f'%media)