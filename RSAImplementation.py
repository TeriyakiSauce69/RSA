def PrimalityTesting(a, x):

    binary = format(a, 'b')

    e = binary[:-1]
    e += "0"



    print(e)
    #e = binary[1:]

    #y = x
    y = 1


    print(e)
    for i in range(len(e)):

        #Added this
        z = y

        y = (y * y) % a

        #Here
        if y == 1 ^ z and y != 1 ^ z and y != (a-1):
            print(a, "is not prime!")
            break

        if e[i] == '1':
            y = (y * x) % a

    if y != 1:
        print(a, "is not prime.")
    else:
        print(a, "is perhaps prime!")

    return y




print('TADA! This the answer', PrimalityTesting(27, 2))