
def getPrimes(num):
    primes = []
    div = 2

    while num >= div:
        if num % div == 0:
            primes.append(div)
            num = num / div
        else:
            div += 1
    return primes
    

def main():
    num = int(input("Please enter a number: "))
    print (f'The prime factors are {getPrimes(num)}')

if __name__ == '__main__':
    main()
