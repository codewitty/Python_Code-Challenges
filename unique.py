import string
import re

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

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
    # Split text string and add to list
    out = result.split()
    dict_save = {}
    count = 0

    for word in out:
        if word in dict_save.keys():
            dict_save[word] += 1
        else:
            dict_save[word] = 1
        count += 1

    print (f'Total word count: {count}')

    sort_orders = sorted(dict_save.items(), key=lambda x: x[1], reverse=True)

    n_items = sort_orders[0:20]

    for group in n_items:
        print(f'{group[0]} appears {group[1]} times')

    file.close()


def main():
    exp = "works.txt"
    print (f'{unique(exp)}')

if __name__ == '__main__':
    main()
