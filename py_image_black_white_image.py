from PIL import Image
from argparse import ArgumentParser

parser = ArgumentParser(description="Convert image to black and white image using python",epilog="""This is a description usage
    python """)

req_parser = parser.add_argument_group('Required Argument')

req_parser.add_argument('-i','--input_image_path',dest='input',type=str,help="specify input_image_path",required=True)
req_parser.add_argument('-o','--output_image_path',dest='output',type=str,help="specify output image_path",required=True)

args= parser.parse_args()

Input = args.input
Output = args.output

class Theme(object):
	"""docstring for Theme"""

	def black_white(self,input_image_path,dithering=True):
		color_image = Image.open(input_image_path)
		if dithering:
			image = color_image.convert('1')
		else:
			image = color_image.convert('1',dither=Image.NONE)
		return image



def main():
	t = Theme()
	image = t.black_white(Input)
	image.save(Output)


if __name__ == '__main__':
	main()
