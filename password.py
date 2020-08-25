import string
import random

def generate_password(length):
    passphrases = {}
    password = ""
    with open("passcode.txt") as myfile:
        for line in myfile:
            passkey, phrase = line.split()
            passphrases[passkey] = phrase.strip("\n")
    print(passphrases)
    for num in range(length):
        code = ""
        for roll in range(5):
            code += str(random.randint(1, 6))
        print(code)
        password += passphrases[code] + " "

    return password.rstrip()
 

def main():
    print(f'Your password is: {generate_password(10)}')

if __name__ == '__main__':
    main()
