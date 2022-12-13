def PrimalityTesting(x, expo, n):

    binary = format(expo, 'b')
    e = binary[1:]
    y = x

    for i in range(len(e)):

        #Added this
        z =  y

        y = (y * y) % n

        #Here
        if  1 ^ z != 1 ^ z != (n-1):
            print(n, "is not prime!")
            break

        if e[i] == '1':
            y = (y * x) % n

    if y != 1:
        print(n, "is not prime.")
    else:
        print(n, "is perhaps prime!")

    return y




print('TADA! This the answer', PrimalityTesting(23, 43, 36))