from collections import defaultdict
def netflow(filename):
	ipdict=defaultdict(dict)
	with open(filename, 'r') as file:
		for line in file:
			words= line.split(' -> ')
			source = words[0].split(':')
			source_ip = source[0]
			dest = words[1].split(':')
			dest_ip = dest[0]
			dest_port = dest[1]
			if dest_ip not in ipdict[source_ip].keys():
				ipdict[source_ip][dest_ip] = [dest_port]
			else:
				ipdict[source_ip][dest_ip].append(dest_port)
	#print(ipdict)
	for k, v in  ipdict.items():
		for dest_ip, dest_port in v.items():
			if len(set(dest_port)) >= 3:
				print(k)
			else: 
				print('no output')
				break

netflow("netflow.txt")

