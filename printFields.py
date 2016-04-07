# Author - Priyank Palod
with open('dumped_data_authors.txt','r') as AuthorDataset:
	AuthorDataset = AuthorDataset.read()
print "File read"
fields = {}
AuthorDataset = AuthorDataset.split('\n\n##\n')
for Author in AuthorDataset:
	infos = Author.split('\n\n')
	try:
		AuthorName,AuthorID = infos[0].split(' : ')
		for paper in infos[1:]:
			try:
				paper = paper.strip('\n')
				field = paper.split('\n')[2].replace(' : ','')
				if field=='1993':
					print paper
				if field in fields:
					fields[field]+=1
				else:
					fields[field]=1
			except:
				print "Exception : Year coming out to be", paper.split('\n')[1].replace(' : ','')
				# print paper
			
	except Exception, e:
		pass
		# print "Except in", infos
		# print '\n', e, '\n'
print fields
