while True:
    x = input().split()

    y = int(x[0])
    z = int(x[1])

    if (y != z):
        if (y > z ):
            print('Decrescente')
        elif (y < z):
            print('Crescente')
    else:
        break