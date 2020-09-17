# importing module 
import youtube_dl
from argparse import ArgumentParser

parser = ArgumentParser(description="Download YouTube video using python",epilog="""This is a description usage: 
    python down_yt.py -l 1 """)

req_parser = parser.add_argument_group('Required Argument')

req_parser.add_argument('-l','--link',dest='link',type=str,help="specify number of link",required=True) 

args= parser.parse_args()
ydl_opts = {} 

def dwl_vid(): 
	with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
		ydl.download([ZXT]) 


NO_OF_LINKS = int(args.link)
for i in range(0,NO_OF_LINKS):
	LINK = input("Paste the url of the Youtube video: ")
	ZXT = LINK.strip() 
	try:
		dwl_vid()
	except Exception as e:
		print("Other Version may not supported DONE...")

 