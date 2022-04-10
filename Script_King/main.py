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
explorer_camp = Vision('img/image_explorer_v2.jpg')
exp_camp = False
explorer_button = Vision('img/button_explorer.jpg')
exp_camp_but = False
explorer_Secbutton = Vision('img/secondBut_explorer.jpg')
exp_camp_in_but = False
button_envoyer = Vision('img/button_envoyer.jpg')
exp_envoyer = False

button_ville = Vision('img/button_ville.jpg')
exp_ville = False

up_batiment = Vision('img/up_batiment.jpg')
up_button = Vision('img/up_button.jpg')
bat_time = False

bois_ville = Vision('img/bois_ville.jpg')
mais_ville = Vision('img/mais_ville.jpg')
ressource_ville = False

ameliorer_button = Vision('img/ameliorer_button.jpg')

find_baraque = Vision('img/top_Z_unit.jpg')
camp_cac = Vision('img/camp_cac.jpg')
camp_dist = Vision('img/camp_dist.jpg')
entrainer_button = Vision('img/entrainer_button.jpg')
unit_make = False

buble_cac_t1 = Vision('img/unit_buble_cac_t1.jpg')
buble_dist_t1 = Vision('img/unit_buble_dist_t1.jpg')

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
    points_explorer_camp = explorer_camp.find(screenshot, 0.9, 'rectangles')
    if (bat_time == False and unit_make == False and points_explorer_camp and points_explorer_camp[0]):
        pyautogui.moveTo(points_explorer_camp[0][0] + 200, points_explorer_camp[0][1] + 40, 0.2) # le 1 c pour la vitesse
        mouse.click('left')
        print("campement d'explorer find et click " , points_explorer_camp[0])
        exp_camp = True
        sleep(0.2)
    
    points_explorer_button = explorer_button.find(screenshot, 0.9, 'rectangles')
    if (exp_camp == True and bat_time == False and unit_make == False and points_explorer_button and points_explorer_button[0]) :
        pyautogui.moveTo(points_explorer_button[0][0] + 600, points_explorer_button[0][1] + 475, 0.2)
        mouse.click('left')
        print("campement d'explorer bouton " , points_explorer_button[0])
        exp_camp_but = True
        sleep(0.2)

    points_explorer_Secbutton = explorer_Secbutton.find(screenshot, 0.9, 'rectangles')
    if (exp_camp_but == True and bat_time == False and unit_make == False and points_explorer_Secbutton and points_explorer_Secbutton[0]) :
        pyautogui.moveTo(points_explorer_Secbutton[0][0] + 150, points_explorer_Secbutton[0][1] - 50, 0.2)
        mouse.click('left')
        print("explorer bouton " , points_explorer_Secbutton[0])
        exp_camp_in_but = True
        sleep(0.2)

    points_button_envoyer = button_envoyer.find(screenshot, 0.9, 'rectangles')
    if (exp_camp_in_but == True and bat_time == False and unit_make == False and points_button_envoyer and points_button_envoyer[0]) :
        pyautogui.moveTo(points_button_envoyer[0][0] + 150, points_button_envoyer[0][1] - 50, 0.2)
        mouse.click('left')
        print("envoyer bouton " , points_button_envoyer[0])
        exp_envoyer = True
        sleep(0.2)
    
    points_button_ville = button_ville.find(screenshot, 0.9, 'rectangles')
    if (exp_envoyer == True and bat_time == False and unit_make == False and points_button_ville and points_button_ville[0]) :
        pyautogui.moveTo(points_button_ville[0][0] + 175, points_button_ville[0][1] - 50, 0.2)
        mouse.click('left')
        pyautogui.moveTo(900, 600, 0.7)
        print("envoyer bouton " , points_button_ville[0])
        #Scroll
        pyautogui.keyDown('ctrl')
        pyautogui.scroll(3, 0.1)
        pyautogui.keyUp('ctrl')
        exp_ville = True
        sleep(0.2)
    if (exp_ville == True):
        exp_camp = False
        exp_camp_but = False
        exp_camp_in_but = False
        exp_envoyer = False
        exp_ville = False
    # FIN DE PARTI EXPLOR
    
    # Batiment upgrade
    points_up_batiment = up_batiment.find(screenshot, 0.9, 'rectangles')
    if (exp_camp == False and bat_time == False and unit_make == False and points_up_batiment and points_up_batiment[0]) :
        pyautogui.moveTo(points_up_batiment[0][0] + 140, points_up_batiment[0][1] - 80, 0.2)
        mouse.click('left')
        print("batiment find " , points_up_batiment[0])
        bat_time = True
        sleep(0.2)
        
    points_up_button = up_button.find(screenshot, 0.9, 'rectangles')
    if (exp_camp == False and bat_time == True and unit_make == False and points_up_button and points_up_button[0]) :
        print("bat time")
        pyautogui.moveTo(points_up_button[0][0] + 200, points_up_button[0][1] + 430, 0.2)
        mouse.click('left')
        print("batiment up button find " , points_up_button[0])
        sleep(0.2)
        
    points_ameliorer_button = ameliorer_button.find(screenshot, 0.9, 'rectangles')
    if (exp_camp == False and bat_time == True and unit_make == False and points_ameliorer_button and points_ameliorer_button[0]) :
        print("bat time")
        pyautogui.moveTo(points_ameliorer_button[0][0] + 180, points_ameliorer_button[0][1] - 50, 0.2)
        mouse.click('left')
        print("up dans le batiment " , points_ameliorer_button[0])
        bat_time = False
        sleep(0.2)
        pyautogui.moveTo(points_ameliorer_button[0][0] + 180, points_ameliorer_button[0][1] , 0.2)
        
    # fin Batiment upgrade
    
    # Recolte de resource
    
    points_bois_ville = bois_ville.find(screenshot, 0.9, 'rectangles')
    if (exp_camp == False and bat_time == False and unit_make == False and points_bois_ville and points_bois_ville[0]) :
        pyautogui.moveTo(points_bois_ville[0][0] + 140, points_bois_ville[0][1] - 40, 0.2)
        mouse.click('left')
        print("bois find " , points_bois_ville[0])
        ressource_ville = True
        sleep(0.2)
    points_mais_ville = mais_ville.find(screenshot, 0.9, 'rectangles')
    if (exp_camp == False and bat_time == False and unit_make == False and points_mais_ville and points_mais_ville[0]) :
        pyautogui.moveTo(points_mais_ville[0][0] + 140, points_mais_ville[0][1] - 40, 0.2)
        mouse.click('left')
        print("mais find " , points_mais_ville[0])
        ressource_ville = True
        sleep(0.2)
    
    # fin de recolte de resource
    
    # creation d'unite
    
    points_find_baraque = find_baraque.find(screenshot, 0.8, 'rectangles')
    if (exp_camp == False and bat_time == False and points_find_baraque and points_find_baraque[0]) :
        pyautogui.moveTo(points_find_baraque[0][0] + 150, points_find_baraque[0][1], 0.2)
        mouse.click('left')
        print("baraque find " , points_find_baraque[0])
        sleep(0.2)
        unit_make = True
    
    points_camp_cac = camp_cac.find(screenshot, 0.9, 'rectangles')
    if (exp_camp == False and bat_time == False and unit_make == True and points_camp_cac and points_camp_cac[0]) :
        pyautogui.moveTo(points_camp_cac[0][0] + 200, points_camp_cac[0][1] - 20, 0.2)
        mouse.click('left')
        print("camp cac find " , points_camp_cac[0])
        sleep(0.2)
    
    points_camp_dist = camp_dist.find(screenshot, 0.9, 'rectangles')
    if (exp_camp == False and bat_time == False and unit_make == True and points_camp_dist and points_camp_dist[0]) :
        pyautogui.moveTo(points_camp_dist[0][0] + 150, points_camp_dist[0][1], 0.2)
        mouse.click('left')
        print("camp dist find " , points_camp_dist[0])
        sleep(0.2)
        
    points_entrainer_button = entrainer_button.find(screenshot, 0.9, 'rectangles')
    if (exp_camp == False and bat_time == False and unit_make == True and points_entrainer_button and points_entrainer_button[0]) :
        pyautogui.moveTo(points_entrainer_button[0][0] + 200, points_entrainer_button[0][1] - 40, 0.2)
        mouse.click('left')
        print("button entrainer " , points_entrainer_button[0])
        sleep(0.2)
        unit_make = False
        
    #fin de creation
    
    # Recolte les uniter 
    
    points_buble_cac_t1 = buble_cac_t1.find(screenshot, 0.9, 'rectangles')
    if (exp_camp == False and bat_time == False and unit_make == False and points_buble_cac_t1 and points_buble_cac_t1[0]) :
        pyautogui.moveTo(points_buble_cac_t1[0][0] + 200, points_buble_cac_t1[0][1] - 40, 0.2)
        mouse.click('left')
        print("buble cac t1 " , points_buble_cac_t1[0])
        sleep(0.2)
        
    points_buble_dist_t1 = buble_dist_t1.find(screenshot, 0.9, 'rectangles')
    if (exp_camp == False and bat_time == False and unit_make == False and points_buble_dist_t1 and points_buble_dist_t1[0]) :
        pyautogui.moveTo(points_buble_dist_t1[0][0] + 200, points_buble_dist_t1[0][1] - 40, 0.2)
        mouse.click('left')
        print("buble dist t1 " , points_buble_dist_t1[0])
        sleep(0.2)
    # fin de recolte d unité
    
    
    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
