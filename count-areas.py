"""
Image Data Analysis Using Numpy & OpenCV
email:  deeptimalhotra27@gmail.com
author: Deepti Malhotra
"""

import numpy as np
import parseArgs
import cv2
import GrayImageProcessing as gip
import sys


# start processing
if __name__ == '__main__':
    # load the image
    args = parseArgs.parseInputArgs()
    # extract height & width of input image
    dim = args["shape"]

    height, width = dim.split(',')
    obj = gip.count_area ()
    A_out = obj.count_areas ( args["file"] , int(height), int(width))

