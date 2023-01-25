import pygame

def choose_music(number):
    if number==1:
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load("Way.mp3")
        pygame.mixer.music.play()

    elif number==2:
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load("Cold.mp3")
        pygame.mixer.music.play()

    elif number==3:
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load("Party.mp3")
        pygame.mixer.music.play()

    elif number==4:
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load("Travel.mp3")
        pygame.mixer.music.play()
        
print("ENTER THE SERIAL NUMBER OF THE SONG YOU WOULD LIKE TO LISTEN ")
print("1.Way\n"
     "2.Cold\n"
     "3.Party\n"
     "4.Travel\n")
a=int(input())
print(a,"is a good choice")
if a==1:

    print("Playing Way")
    choose_music(1)
elif a==2:

    print("Playing Cold")
    choose_music(2)
elif a==3:

    print("Playing Part")
    choose_music(3)
elif a==4:

    print("Playing Travel")
    choose_music(4)
print("Press 5 to Stop")
b=int(input())
if b==5:
    pygame.mixer.music.stop()
    print("Stopped")