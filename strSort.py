import string

def strSort(expr):
    list1 = expr.split(' ')
    sorted_list = sorted(list1, key=str.casefold)
    out = ""

    for word in sorted_list:
        out += word + " "

    return out.strip()
    

def main():
    exp = input("Please enter an expression: ")
    print (f'{strSort(exp)}')

if __name__ == '__main__':
    main()


'''

OFFICIAL SOLUTION

words = input.split()
words = [w.lower() + w for w in words]
words.sort()
words = 
    
