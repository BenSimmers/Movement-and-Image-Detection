from __future__ import print_function
from typing import Counter, ItemsView

import cv2
import numpy as np
from numpy.lib.polynomial import roots
import pandas as pd
from tkinter import *
from collections import Counter
from openpyxl import *
xcords = []
ycords = []




def main():    
    cap = cv2.VideoCapture(0)

    back_sub = cv2.createBackgroundSubtractorMOG2(history=700, 
        varThreshold=25, detectShadows=True)


    kernel = np.ones((20,20),np.uint8)

    while(True):
        ret, frame = cap.read()
        fg_mask = back_sub.apply(frame)
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)
        fg_mask = cv2.medianBlur(fg_mask, 5) 
        _, fg_mask = cv2.threshold(fg_mask,127,255,cv2.THRESH_BINARY)

        fg_mask_bb = fg_mask
        contours, hierarchy = cv2.findContours(fg_mask_bb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]
        areas = [cv2.contourArea(c) for c in contours]
 
        # If there are no countours
        if len(areas) < 1:
 
            # Display the resulting frame
            cv2.imshow('frame',frame)
 
            # If "q" is pressed on the keyboard, 
            # exit this loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
 
            # Go to the top of the while loop
            continue
 
        else:
            # Find the largest moving object in the image
            max_index = np.argmax(areas)
 
        # Draw the bounding box
        cnt = contours[max_index]
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
 
        # Draw circle in the center of the bounding box
        x2 = x + int(w/2)
        y2 = y + int(h/2)
        cv2.circle(frame,(x2,y2),4,(0,255,0),-1)
 
        # Print the centroid coordinates (we'll use the center of the
        # bounding box) on the image
        text = "x: " + str(x2) + ", y: " + str(y2)
        cv2.putText(frame, text, (x2 - 10, y2 - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        print(f"x: {x2} y: {y2}")
        xcords.append(x2)
        ycords.append(y2)


        # Display the resulting frame
        cv2.imshow('frame',frame)

        # If "q" is pressed on the keyboard, 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # Close down the video stream
    cap.release()
    cv2.destroyAllWindows()










############################################################################################
    len(xcords)
    outliers=[]
    def detect_outlier(data_1):

        threshold=3
        mean_1 = np.mean(data_1)
        std_1 =np.std(data_1)


        for y in data_1:
            z_score= (y - mean_1)/std_1 
            if np.abs(z_score) > threshold:
                outliers.append(y)
        return outliers



    outlier_datapoints = detect_outlier(xcords)
    print(f"outlier is: {outlier_datapoints}")
    sorted(xcords)




    q1, q3= np.percentile(xcords,[25,75])


    iqr = q3 - q1

    lower_bound = q1 - (1.5 * q1)
    upper_bound = q3 + (1.5 * q3)

    print(f"Lower bound is: {lower_bound}")
    print(f"Upper bound is: {upper_bound}")
################################################################################################
    len(ycords)

    outliers2=[]
    def detect_outlier2(data_2):

        thresh_=3
        mean_2 = np.mean(data_2)
        std_2 =np.std(data_2)


        for y in data_2:
            z_score= (y - mean_2)/std_2 
            if np.abs(z_score) > thresh_:
                outliers2.append(y)
        return outliers2



    outlier_datapoints = detect_outlier2(ycords)
    print(f"outlier is: {outlier_datapoints}")
    sorted(ycords)

    q1_, q3_= np.percentile(ycords,[25,75])


    iqr_ = q3_ - q1_

    lower_bound_ = q1_ - (1.5 * q1_)
    upper_bound_ = q3_ + (1.5 * q3_)

    print(f"Lower bound is: {lower_bound_}")
    print(f"Upper bound is: {upper_bound_}")

    print("                                                                   ")
##########################################################################

    print(xcords)
    print(ycords)
    print("###################################################################")


    xcounter = Counter(xcords)
    ycounter = Counter(ycords)

    most_common_x = xcounter.most_common(1)
    most_common_y = ycounter.most_common(1)

    initial_x = max(set(xcords), key = xcords.count)
    inital_y = max(set(ycords), key = ycords.count)

    print('the most common x value is: ', most_common_x)
    print('the most common y value is: ', most_common_y)
    print("*******************************************")





















if __name__ == '__main__':
    print(__doc__)
    main()