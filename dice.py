import random

def roll_dice(*args, trials = 1000000):
    d_dict = {}
    temp_dict = {}

    for roll in range(trials):
        sums = 0
        for arg in args:
            sums += (random.randint(1, arg))
        if sums in d_dict:
            d_dict[sums] += 1
        else:
            d_dict[sums] = 1

    print (f'\nOUTCOME\tPROBABILITY')
    for outcome in range (len(args), sum(args) + 1):
        print(f'{outcome}\t{d_dict[outcome]*100/trials:0.2f}')

def main():
    roll_dice(4,6,6)

if __name__ == '__main__':
    main()
