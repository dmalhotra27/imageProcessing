# File to perform segmentation of given gray scaled image into different regions based on shade
# and maintain count per shade

import numpy as np
import cv2

# extended display showing count of different areas in gray scale image per index for readability
def extended_display(arr):
    index = 0
    print("Shade --> Count" )
    print("---------------")
    for element in arr:
        print(f'{index} --> {int(element)}\n')
        index += 1

# to display count of different areas in gray scale image
def display(arr):
    for element in arr:
        print(int(element))


# function to retrieve (threshold value , max value, threshold type) per gray shade retrieved to extract
# binary image from grayscale through threshold process
def get_threshold_maxVal_perGrayShade(shade):
    if shade == 0: #black
        return 128,255, cv2.THRESH_BINARY_INV
    elif shade == 255: #white
        return 225,255, cv2.THRESH_BINARY
    else:
        return shade+10, 255, cv2.THRESH_TOZERO_INV


# function to count areas per shade retrieved
def count_areas_per_shade(levels, isBin, image, gray):
    np_count = np.zeros ( [256 , 1] )
    for shade in levels:
        threshold, maxVal, thres_type = get_threshold_maxVal_perGrayShade(shade)

        if isBin == 0:
            canvas_str = np.zeros(image.shape, np.uint8)

        ret,thresh = cv2.threshold(gray,threshold,maxVal,thres_type)
        erode = cv2.erode ( thresh , None , iterations=3 )
        contours_str = "contours" + str(shade)
        contours,hierarchy = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        count = len(contours)
        # print(f'{contours_str}: {count}')
        np_count[shade] = count
        if isBin ==0:
            for cont in contours:
                cv2.drawContours ( canvas_str , cont , -1 , (0 , 255 , 0) , 3 )

            # *** uncomment this code to view different contours per gray scale ***
            #cv2.imshow ( contours_str , canvas_str )
            #cv2.waitKey ( 0 )

    return np_count
