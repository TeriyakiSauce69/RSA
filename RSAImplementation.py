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




#Primality Test. Seems to kinda work. Could use some work. Taken from class slides.
def PrimalityTesting(a, x):
    print("Testing with",x,".")

    binary = format(a, 'b')

    e = binary[:-1]
    e += "0"

    #print(e)
    #e = binary[1:]

    #y = x
    y = 1

    #print(e)
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
    #print(y)
    return y

import math, time, random


#Euclid Algorithm to find GCD of two Inputs, and get Multplicative Inverse. I didn't understand the implementation from
#Slides well. I implemented what I found on the bottom of this site, http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html.
#Seems to get the job done.
def Euclid(x,y):
    #print('i',"\t",'q',"\t", 'm',"\t", 'n',"\t", 'r',"\t", 't')
    #print('-------------------------------------------------------------')

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

    #print("This is the multplicative inverse, ti , we care about! ", (t - (lastt * list[i - 2])) % still_x)
    multplicative_inverse = (t - (lastt * list[i - 2])) % still_x
    #print(multplicative_inverse)


    #print('STOP, the GCD between these two integers is:', x)
    return x, multplicative_inverse

def main():
    #Get two random numbers that may be prime, x and y.

    while True:
        p = getRandomPrime()
        print("\n")

        twenty_as = []
        while True:
            d = random.randrange(1, p)
            if d not in twenty_as:
                twenty_as.append(d)
            if len(twenty_as) == 20:
                break
        for a in twenty_as:
            PrimalityTesting(p, a)
        break

    print("\n")

    while True:
        q = getRandomPrime()
        print("\n")

        twenty_as2 = []
        while True:
            z = random.randrange(1, q)
            if z not in twenty_as2:
                twenty_as2.append(z)
            if len(twenty_as2) == 20:
                break
        for k in twenty_as2:
            PrimalityTesting(q, k)
        break


    print("\n")

    n = 0
    if p != q:
        n = p * q
    else:
        print("P and Q are equal. Stop and rerun this please!")

    #Euclid(37,29)
    for e in range(3,2000):
        x, multplicative_inverse = Euclid(e,n)
        if x == 1:
            print(e, "and", n, "are relatively prime. The Multiplicative inverse is:", multplicative_inverse )
            print("\n")
            print("p = ", p, "q = ", q, "n = ", n, "e = ", x, "d = ", multplicative_inverse)
            break


if __name__ == "__main__":
    main()