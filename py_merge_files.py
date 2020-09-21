from argparse import ArgumentParser

parser = ArgumentParser(description="",epilog="""This is a description usage 
    python py_merge_files.py""")

req_parser = parser.add_argument_group('Required Argument')

req_parser.add_argument('-n','--number',dest='number',type=str,help="specify number of files to merge",required=True)
req_parser.add_argument('-o','--output',dest='output',type=str,help="specify output filename",required=True)

args= parser.parse_args()
number = int(args.number)
file_list = []


for i in range(0,number):
	n = input(f"Enter the file name {i+1} : ")
	file_list.append(n)

with open(args.output, "w") as outputfile:
	for i in file_list:
		try:
			with open(i) as inputfile:
				outputfile.write(inputfile.read())
		except:
			print(f"Error file not FOUND!.....")

		outputfile.write("\n")
