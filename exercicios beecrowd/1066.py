pos = 0
neg = 0
odd = 0
even = 0

for i in range(5):
    x = int(input())
    if (x > 0):
        pos += 1
    if (x < 0):
        neg += 1
    if (x % 2) == 0 :
        even += 1
    else:
        odd += 1
print('{} valor(es) par(es)'.format(even))
print('{} valor(es) impar(es)'.format(odd))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))