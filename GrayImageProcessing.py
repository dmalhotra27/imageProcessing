import cv2
import segmentation as seg
import preprocessingImage as ppi


# class containing logic for counting areas in a grayscale image & process it in 2 stages
# stage 1: pre-processing
# stage 2: segmentation
class count_area:

    # function to display properties of gray image
    def properties_image(gray):
        print ( 'Type of the image : ' , type ( gray ) )
        print ( 'Shape of the image : {}'.format ( gray.shape ) )
        print ( 'Image Height {}'.format ( gray.shape[0] ) )
        print ( 'Image Width {}'.format ( gray.shape[1] ) )
        print ( 'Dimension of Image {}'.format ( gray.ndim ) )
        print ( 'Image size {}'.format ( gray.size ) )

    def count_areas(self, fileName, height, width):
        # stage1 : preprocessing
        image, gray , isBin = ppi.ReadImage ( fileName , int ( height ) , int ( width ) )
        levels = ppi.countDistinctGrayLevelsInImage ( gray )

        # *** uncomment this code to view original image ***
        # if isBin == 0:
        #    cv2.imshow ( "Original" , image )

        # stage2: segmentation
        countArr = seg.count_areas_per_shade ( levels , isBin , image , gray )
        seg.display ( countArr )