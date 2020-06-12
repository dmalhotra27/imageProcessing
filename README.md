AnalyzingGrayScaleImage Exercise
------------------------------------------------
Analyzing the number of colored ares in an image

Exercise: Input a grey-scale image, count number of colored areas in that image. Output should be contents of array with corresponding count 
of each gray shade retrieved.

Design:
--------
The logic has been developed as per below steps:

1) Parse Arguments
To parse command line arguments & retrieve input file along with dimensions -- height & width of image

2) Preproceesing Stage
To read given gray scaled image which can be either binary or jpg/jpeg/png format. Identify distinct gray scaled pixels in an image along with corresponding 
count of occurences in an image

3) Segmentation
Segmentation logic deals with identifying different regions in a gray scaled image per gray shade determined in pre-processing stage. 

Above logic (step 2 & step 3) is part of class "count_area" of 'GrayImageProcessing.py' which is invoked through Interface 'count-areas.py'. 
The function count_areas() is used to count the areas for different grayscale levels and output them.

Implementation:
----------------
1. Get the number of distinct grayscale levels
2. Loop each grayscale level, fetch corresponding threshold value , max value & threshold type for the shade
3. Erode the image to have accurate counts considering overlapping regions
3. Find regions/areas corresponding to each grayscale level
4. Save the numbers of areas for each grayscale level in an Array. End the loop of each grayscale & output the array.

Additional functionality available:
------------------------------------
1) Region/area corresponding to each grey scale level determined can be displayed

For this, uncomment the code in function 'count_areas_per_shade(...)' of 'segmentation.py' as mentioned in 3 asterisks "***"
Also for original image, uncomment the code in function 'count_areas(...)' of 'GrayImageProcessing.py' as mentioned in 3 asterisks "***"

2) To view additional properties of input image
Invoke function 'properties_image' in 'GrayImageProcessing.py'

3) To view enhanced display of count of regions per gray shade corresponding to index in an array
Invoke function 'extended_display(...)' of 'segmentation.py'

Usage:
-------

Input: Image (.bin or .png/.jpeg/.jpg image) , height and width.

Output: array of 256 unsigned int numbers, each of them being a count of areas colored with the corresponding shade of grey.

Sample Images: 'shades-of-grey.png' , 'sample.bin', 'left01.jpg'

Syntax for invocation:
-----------------------

> python count-areas.py <filename> --shape <height>,<width>

For example:

> python count-areas.py shades-of-grey.png --shape 250,250