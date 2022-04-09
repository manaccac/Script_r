from multiprocessing.connection import wait
import cv2 as cv
import numpy as np
import os
from time import sleep
from windowcapture import WindowCapture
from vision import Vision

# mouse move
import win32api
from win32con import *
import mouse


import pyautogui

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# WindowCapture.list_window_names()
# exit()

# initialize the WindowCapture class
wincap = WindowCapture('NoxPlayer')
# initialize the Vision class
explorer_camp = Vision('image_explorer_v2.jpg')
exp_camp = False
explorer_button = Vision('button_explorer.jpg')
exp_camp_but = False
explorer_Secbutton = Vision('secondBut_explorer.jpg')
exp_camp_in_but = False
button_envoyer = Vision('button_envoyer.jpg')
exp_envoyer = False

button_ville = Vision('button_ville.jpg')
exp_ville = False


'''
# https://www.crazygames.com/game/guns-and-bottle
wincap = WindowCapture()
vision_gunsnbottle = Vision('gunsnbottle.jpg')
'''

# loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    

    cv.imshow('Matches', screenshot)
    # display the processed image
    
    # parti explore d'ici a
    points_explorer_camp = explorer_camp.find(screenshot, 0.5, 'rectangles')
    if (points_explorer_camp and points_explorer_camp[0]):
        pyautogui.moveTo(points_explorer_camp[0][0] + 125, points_explorer_camp[0][1] + 125, 0.7) # le 1 c pour la vitesse
        mouse.click('left')
        print("campement d'explorer find et click " , points_explorer_camp[0])
        exp_camp = True
        sleep(0.5)
    
    points_explorer_button = explorer_button.find(screenshot, 0.5, 'rectangles')
    if (exp_camp == True and points_explorer_button and points_explorer_button[0]) :
        pyautogui.moveTo(points_explorer_button[0][0] + 600, points_explorer_button[0][1] + 475, 0.5)
        mouse.click('left')
        print("campement d'explorer bouton " , points_explorer_button[0])
        exp_camp_but = True
        sleep(0.5)

    points_explorer_Secbutton = explorer_Secbutton.find(screenshot, 0.5, 'rectangles')
    if (exp_camp_but == True and points_explorer_Secbutton and points_explorer_Secbutton[0]) :
        pyautogui.moveTo(points_explorer_Secbutton[0][0] + 150, points_explorer_Secbutton[0][1] - 50, 0.5)
        mouse.click('left')
        print("explorer bouton " , points_explorer_Secbutton[0])
        exp_camp_in_but = True
        sleep(0.5)

    points_button_envoyer = button_envoyer.find(screenshot, 0.5, 'rectangles')
    if (exp_camp_in_but == True and points_button_envoyer and points_button_envoyer[0]) :
        pyautogui.moveTo(points_button_envoyer[0][0] + 150, points_button_envoyer[0][1] - 50, 0.5)
        mouse.click('left')
        print("envoyer bouton " , points_button_envoyer[0])
        exp_envoyer = True
        sleep(0.5)
    
    points_button_ville = button_ville.find(screenshot, 0.5, 'rectangles')
    if (exp_envoyer == True and points_button_ville and points_button_ville[0]) :
        pyautogui.moveTo(points_button_ville[0][0] + 175, points_button_ville[0][1] - 50, 0.5)
        mouse.click('left')
        pyautogui.moveTo(900, 600, 0.7)
        print("envoyer bouton " , points_button_ville[0])
        #Scroll
        pyautogui.keyDown('ctrl')
        pyautogui.scroll(3, 0.1)
        pyautogui.keyUp('ctrl')
        exp_ville = True
        sleep(0.5)
    if (exp_ville == True):
        exp_camp = False
        exp_camp_but = False
        exp_camp_in_but = False
        exp_envoyer = False
        exp_ville = False
    # FIN DE PARTI EXPLOR
    
    
    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
