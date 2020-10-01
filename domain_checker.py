import whois
from argparse import ArgumentParser


parser = ArgumentParser(description="",epilog="""This is a description usage 
    python domain_checker.py -d google.com """)

req_parser = parser.add_argument_group('Required Argument')



req_parser.add_argument('-d','--domain',dest='domain',type=str,help="specify domain name")


req_parser.add_argument('-l','--list',dest='list',type=str,help="specify the domain list")

req_parser.add_argument('-o','--output',dest='output',type=str,help="specify output filename")


args= parser.parse_args()

domain = args.domain
list_filename = args.list
output = args.output

def domain_checker(dom):
	try:
		w = whois.whois(dom)
		domain = w.domain_name
		if domain is not None:
			print(f"{dom} : Domain is available")
			if output:
				a = f"{dom} : Domain is available"
				output_file(a)

	except:
		print(f" {dom}: Domain is not available")
		if output:
			a = f"{dom} : Domain is not available"
			output_file(a)



def output_file(res):
	with open(output,"a") as f:
		f.write(res)
		f.write("\n")
		f.close()


if domain:
	domain_checker(domain)

elif list_filename:
	with open(list_filename,"r") as f:
		domain_list = f.readlines()
	for d in domain_list:
		a = d.strip() 
		domain_checker(a)

else:
	print("SPECIFY THE DOMAIN NAME!.............")
