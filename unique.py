import string
import re

def unique(file_name):
    with open(file_name, 'r') as file:
        data = file.read().replace('\n', '')
    data = data.lower()
    # Create string
    remove = string.punctuation
    # don't remove hyphens
    remove = remove.replace("-", "") 
    # don't remove hyphens
    remove = remove.replace("'", "") 
    # Make the pattern
    pattern = r"[{}]".format(remove)
    # Strip punctuation from the input
    result = re.sub(pattern, " ", data)
    file.close()

    return result

def main():
    exp = "works.txt"
    print (f'{unique(exp)}')

if __name__ == '__main__':
    main()
