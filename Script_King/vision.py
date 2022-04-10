import cv2 as cv
import numpy as np
from time import sleep
import pyautogui
import pydirectinput
from pynput.keyboard import Key, Controller

import mouse

keyboard = Controller()

class Vision:

    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None

    # constructor
    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):
        # load the image we're trying to match
        # https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

        # Save the dimensions of the needle image
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def find(self, haystack_img, threshold, debug_mode=None):
        points = []
        # pydirectinput.moveTo(350, 200)
        # run the OpenCV algorithm
        result = cv.matchTemplate(haystack_img, self.needle_img, self.method)
        # print(threshold)

        # threshold = 0.9
        # Get the all the positions from the match result that exceed our threshold
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        
        #print(locations)
        
        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        
        i = 0
        if (locations):
            while (i != len(locations)):
                bleu = list(locations)
                bleu[i] = (locations[i][0] + 65, locations[i][1] + 125)
                locations = tuple(bleu)
                i +=1   
        
        for loc in locations:
            top_left = loc
            
            points = locations
            # print(locations[0])
            # pydirectinput.moveTo(x=locations[0][0], y=locations[0][1])
            # mouse.click('right')
            # pydirectinput.click(button='right')
            
            bottom_right = (top_left[0] + 2,top_left[1] + 2)
            cv.rectangle(haystack_img, top_left, bottom_right, color=line_color, 
                                lineType=line_type, thickness=2)

            
        cv.imshow('Matches', haystack_img)

        return points
