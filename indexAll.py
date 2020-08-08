import string

def indexAll(list1, num):
    indices = []
    for i in range(len(list1)):
        if list1[i] == num:
            indices.append([i])
        elif isinstance(list1[i], list):
            for index in indexAll(list1[i], num):
                indices.append([i] + index)
    return indices

def main():
    exp = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print (f'{indexAll(exp, 2)}')

if __name__ == '__main__':
    main()

