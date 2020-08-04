def palindrome(expr):
    pal = expr.lower()
    a = 0
    b = len(expr) - 1

    while a < b:
        if pal[a] == pal[b]:
            a += 1
            b -= 1
        else:
             return False
    return True
    

def main():
    exp = input("Please enter an expression: ")
    print (f'{palindrome(exp)}')

if __name__ == '__main__':
    main()
