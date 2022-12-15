import random, math, time


def getRandomPrime():
    random.seed()

    #Initialize binary string
    prime_number_seed = 1
    prime_number= format(prime_number_seed,'b')
    #print(prime_number)

    #Iterate five times to get five random integers
    #And then extract their LSB to append to the prime number.
    for i in range(5):
        x = random.randint(1,100)
        binary = format(x, 'b')
        #print(binary)

        y = x & 1
        prime_number += str(y)
        print("Random Binary Number:",binary, "LSB",y)
    #Add last, 1, bit.
    prime_number += str(1)
    prime_number = "0000000000000000000000000" + prime_number

    prime_number_int = int(prime_number, 2)
    print("Final prime in 32 bit format:", prime_number, "\nIn integer form:", prime_number_int)

    return prime_number_int







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

import math, time, random


#Euclid Algorithm to find GCD of two Inputs
def Euclid(x,y):
    print('i',"\t",'q',"\t", 'm',"\t", 'n',"\t", 'r',"\t", 't')
    print('-------------------------------------------------------------')

    t, lastt = 0, 1
    #print("t, lastt" , t, lastt)

    p = 0

    if x < y:
        x,y = y,x
    still_x = x

    i = 0

    list = []
    while y != 0:
        r = x % y

        print(i,"\t", (x // y),"\t", x,"\t", y,"\t", r,"\t", t)
        list.append((x // y))

        i += 1

        if i > 2:
            #print(t,"should be 0,", lastt,"Should be 1", list[i - 3])
            #print("Should be -1",(t - (lastt * list[i - 3])))
            #print("Should be 26", still_x)
            p = (t - (lastt * list[i - 3])) % still_x

            #print(list[i - 3])

            #print("Here", p)

            t, lastt = lastt, p
            #print("t, lastt", t, lastt)

        x = y
        y = r
    #print(t, lastt, list[i-3],still_x)

    print("This is the multplicative inverse, ti , we care about! ", (t - (lastt * list[i - 2])) % still_x)
    multplicative_inverse = (t - (lastt * list[i - 2])) % still_x
    print(multplicative_inverse)

    #print(0-3)
    #print("This should be 25",-1 % 26)

    # for z in list:
    #     print(z)
    # print("DIS", list[5 - 3])

    print('STOP, the GCD between these two integers is:', x)
    return x, multplicative_inverse

def main():
    #x = getRandomPrime()
    #print("\n")
    #y = getRandomPrime()

    #print("\n")
    # print('TADA! This the answer', PrimalityTesting(x, 2))
    #PrimalityTesting(x, 2)
    #print("\n")

    #Euclid(37,29)
    for e in range(3,2000):
        x, multplicative_inverse = Euclid(e,9504)
        if x == 1:
            print(e, "and", 9504, "are relatively prime. The Multiplicative inverse is:", multplicative_inverse )
            break

if __name__ == "__main__":
    main()