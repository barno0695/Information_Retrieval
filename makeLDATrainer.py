# Author - Priyank Palod
with open('reduced_authors.txt','r') as AuthorDataset:
	AuthorDataset = AuthorDataset.read()
print "File read"
authorBag = ''
AuthorDataset = AuthorDataset.split('\n\n##\n')
for Author in AuthorDataset:
	infos = Author.split('\n\n')
	try:
		AuthorName,AuthorID = infos[0].split(' : ')
		for paper in infos[1:]:
			try:
				paper = paper.strip('\n')
				title = paper.split('\n')[3].replace(' : ','')
				authorBag += title
			except:
				print "Exception : Year coming out to be", paper.split('\n')[1].replace(' : ','')
				# print paper
			
	except Exception, e:
		pass
		# print "Except in", infos
		# print '\n', e, '\n'
	authorBag += '\n'
with open('LDAinput_reduced.txt','w') as LDAFile:
	LDAFile.write(authorBag)