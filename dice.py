import random

def roll_dice(*args):
    d_dict = {}
    sums = 0
    for num in range(0, 1000000):
        for arg in args:
            sums += (random.randint(1, arg))
        if sums in d_dict:
            d_dict[sums] += 1
        else:
            d_dict[sums] = 1
    for key, value in d_dict.items():
        print(f'{key} : {(value/10000)} \n')
    

def main():
    roll_dice(4,6,6)

if __name__ == '__main__':
    main()
