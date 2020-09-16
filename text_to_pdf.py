#!/usr/bin/python3
# Convert text file to pdf file 

from fpdf import FPDF 
from argparse import ArgumentParser

parser = ArgumentParser(description="CONVERT TEXT TO PDF",epilog="""This is a description usage
   python3 text_to_pdf.py -f <filename>  -o <output filename>""")

req_parser = parser.add_argument_group('Required Argument')

req_parser.add_argument('-f','--filename',dest='filename',type=str,help="specify filename",required=True)
req_parser.add_argument('-o','--output',dest='output',type=str,help="specify output pdf filename",required=True)

args= parser.parse_args()

pdf_file = args.filename
output_file = args.output

pdf = FPDF() 
 
pdf.add_page() 

pdf.set_font("Arial", size = 15) 

 
f = open(pdf_file, "r") 

 
for x in f: 
	pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 

 
pdf.output(output_file)
