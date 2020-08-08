import string
import time
import random


def waitingGame():
    while True:
        num = random.randrange(2,5)
        print(f'Your target time is {num} seconds.')
        input("---Press enter to begin--- \n")
        start= time.perf_counter()
        input('....Press enter again after {} seconds....'.format(num))
        elapsed = time.perf_counter() - start

        print(f'Time elapsed: {elapsed:.03f}seconds')

        if (elapsed == num):
            print (f'Great job. Perfect timing')
        elif (elapsed > num):
            print (f'{elapsed-num:.03f} seconds too slow.')
        else:
            print (f'{num - elapsed:.03f} seconds too fast.')
        check = (input(f'Would you like to play again?\nEnter Y if Yes or N if no.\n')).upper()
        if check != "Y":
            break
    return 0


def main():
    exp = input("Press enter to play the waiting game: ")
    waitingGame()

if __name__ == '__main__':
    main()
