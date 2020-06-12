# File to pre-process the Input image -- read the file & determine count of distinct gray levels in an image

import cv2
import numpy as np
import sys

# function to read binary file given as input
def ReadBin(filename , height , width):
    try:
        binfile = open ( filename , 'rb' )
        gray = np.fromfile (binfile , dtype=np.ubyte).reshape(height, width)
        return gray
    except cv2.error as e:
        print ( "cv exception caught: {}".format ( e ) )
        print ( "Exiting!!!" )
        sys.exit ( 1 )
    except ValueError as err:
        print ( "Value error exception caught: {}".format ( err ) )
        print ( "Exiting!!!" )
        sys.exit ( 1 )

# function to read image
def ReadImage(filename , height , width):
    try:
        image = cv2.imread ( filename )
        if filename[-3:] == 'png' or filename[-3:] == 'jpg' or filename[-3:] == 'peg':
            gray = cv2.cvtColor ( image , cv2.COLOR_BGR2GRAY )
            isBin = 0
        elif filename[-3:] == 'bin':
            gray = ReadBin ( filename , height , width )
            isBin = 1

        return image, gray, isBin
    except cv2.error as e:
        print("cv exception caught: {}".format(e))
        print("Exiting!!!")
        sys.exit(1)
    except ValueError as err:
        print ( "Value error exception caught: {}".format ( err ) )
        print ( "Exiting!!!" )
        sys.exit ( 1 )

# function to count how many grayscale levels with corresponding counts.
def countDistinctGrayLevelsInImage(arr):
     arr = np.array(arr)
     keys = np.unique(arr)

     result = {}
     for key in keys:
        occurrences = np.count_nonzero ( arr == key )
        result[key] = occurrences

     return result

