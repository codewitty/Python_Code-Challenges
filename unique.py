import re
from collections import Counter

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def unique(file_name):
    with open(file_name, 'r') as file:
        data = re.findall(r"[0-9a-zA-Z-']+", file.read())
        data = [words.upper() for words in data]
        print (f'Total word count: {len(data)}')

    dict_save = Counter() 

    for word in data:
        dict_save[word] += 1

    sort_orders = sorted(dict_save.items(), key=lambda x: x[1], reverse=True)
    n_items = sort_orders[0:20]

    for group in n_items:
        print(f'{group[0]} appears {group[1]} times')
    #Another way to count appearences:
    """
    for word in dict_save.most_common[20]:
        print(f'{word[0]} appears {word[1]} times')
    """

    file.close()


def main():
    exp = "works.txt"
    print (f'{unique(exp)}')

if __name__ == '__main__':
    main()
    """
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
    # Split text string and add to list
    out = result.split()
    """
