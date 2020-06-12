# import the necessary packages
import argparse


#  function to parse the command line arguments
def parseInputArgs():
     ap = argparse.ArgumentParser()
     ap.add_argument('file')
     ap.add_argument("--shape", required=True,type=str,
		  help="height and width of input image")
     args = vars(ap.parse_args())
     return args




