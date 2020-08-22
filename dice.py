import random

def roll_dice(*args):
    d_dict = {}
    for num in range(0, 1000):
        sums = 0
        temp_dict = {}
        for arg in args:
            for num in range(1, arg):
                if num in d_dict:
                    d_dict[num] += 1
                else:
                    d_dict[num] = 1
        for key, value in temp_dict.items():
            d_dict[value] = 0

        for arg in args:
            sums += (random.randint(1, arg))
        #if sums in d_dict:
            #d_dict[sums] += 1
        #else:
            d_dict[sums] = 1
    for key, value in d_dict.items():
        print(f'{key} : {(value/10)} \n')
    

def main():
    roll_dice(4,6,6)

if __name__ == '__main__':
    main()
