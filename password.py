import string

def generate_password(length):
    passphrases = {}
    with open("passcode.txt") as myfile:
        for line in myfile:
            passkey, phrase = line.partition("\t")[::2]
            passphrases[passkey.strip()] = phrase.strip("\n")
    

def main():
    generate_password(5)

if __name__ == '__main__':
    main()
