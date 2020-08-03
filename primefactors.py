
def getPrimes(num):
    primes = []

    while num != 0:
        if num % 2 == 0:
            primes.append(2)
            num = num - (num % 2)
        elif num % 3 == 0:
            primes.append(3)
            num = num - (num % 3)
        elif num % 5 == 0:
            primes.append(5)
            num = num - (num % 5)
        elif num % 7 == 0:
            primes.append(7)
            num = num - (num % 7)
    
    if num > 0:
        p_list = [num, 1]
        return p_list
    else:
        return primes
    

def main():
    num = int(input("Please enter a number: "))
    print (f'The prime factors are {getPrimes(num)}')

if __name__ == '__main__':
    main()
