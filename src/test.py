







if __name__ == '__main__':
	pid="LALALA"
	pid2="NONONON"
	string="MATCH p=(p1:Prot)-[j:LINK]-(p2:Prot)where p1.prot_id='"+pid+"' return p LIMIT 30 UNION MATCH p=(p1:Prot)-[j:LINK]-(p2:Prot) where p1.prot_id='"+pid2+"' return p LIMIT 30"
	print(string)