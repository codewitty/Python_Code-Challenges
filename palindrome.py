import string

def palindrome(expr):
    expr = expr.lower()
    expr = expr.replace(" ", "")
    expr = expr.translate(str.maketrans('', '', string.punctuation))
    pal = expr[::-1]

    return expr == pal
    

def main():
    exp = input("Please enter an expression: ")
    print (f'{palindrome(exp)}')

if __name__ == '__main__':
    main()
