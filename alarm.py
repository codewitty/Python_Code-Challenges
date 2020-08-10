from playsound import playsound

def set_alarm(time, sound, message):

    playsound(sound)
    print(f'{message}')



def main():
    set_alarm(25, "upbeat.mp3", "Wake UP!!!!")

if __name__ == '__main__':
    main()
