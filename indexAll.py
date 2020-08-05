import string

def strSort(expr):
    list1 = expr.split(' ')
    words = sorted(list1, key=str.casefold)

    return ' '.join(words)

def main():
    exp = input("Please enter an expression: ")
    print (f'{strSort(exp)}')

if __name__ == '__main__':
    main()


'''

OFFICIAL SOLUTION

def strSort(input):
    words = input.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)
''' 
