import cv2
import pyfiglet
from argparse import ArgumentParser

parser = ArgumentParser(description="Convert image to black and white image using python",epilog="""This is a description usage
    python py_cimg_bwimg.py -i ./images.jpeg -o bb.jpeg""")

req_parser = parser.add_argument_group('Required Argument')

req_parser.add_argument('-i','--input_image_path',dest='input',type=str,help="specify input_image_path",required=True)
req_parser.add_argument('-o','--output',dest='output',type=str,help="specify output filename to save",required=True)

args= parser.parse_args()

Input = args.input
Output = args.output

class Theme(object):
	"""docstring for Theme"""
	def __init__(self):
		self.key  = "Press Any Key"
		

	def Banner(self,name):
		banner = pyfiglet.figlet_format(name, font = "bulbhead" )
		print(banner)

	def black_white(self,input_image_path):
		try:
			image = cv2.imread(input_image_path)
			cv2.imshow('Original', image)
			self.Banner(self.key)
			cv2.waitKey(0)
			gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
			cv2.imshow('Grayscale', gray_image)
			self.Banner(self.key) 
			cv2.waitKey(0)
			cv2.destroyAllWindows()
			cv2.imwrite(Output,gray_image) 
			
		except:
			pass
		



def main():
	t = Theme()
	image = t.black_white(Input)
	




if __name__ == '__main__':
	main()
