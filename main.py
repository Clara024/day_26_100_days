import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    print('Type in "2" to restart the song and program and type "3" to close program')
    Restart = int(input(''))

while True:
  # clear the screen 
    os.system('clear')
  # Show the menu
    print('Welcome to the Music Player!')
    time.sleep(2)
    print('Press 1 to play audio')
    time.sleep(3)
    print('Press 2 to stop and restart')
    time.sleep(3)
    print('Type 3 to end program')
    time.sleep(3)
  # take user's input
    UserPlay = int(input('  ->  '))
    if UserPlay == 1:
     print('here are the nice tunes! ')
     play()
    elif UserPlay == 2:
     print('You have to play the music first')
    elif UserPlay == 3:
     break
    else:
     print('Sorry, it is not available')

  # check whether you should call the play() subroutine depending on user's input
    if True:
      play()

