with open('reduced_authors.txt','r') as AuthorDataset:
	AuthorDataset = AuthorDataset.read()
print "File read"
LTE2005 = []
G2005 = []
AuthorDataset = AuthorDataset.split('\n\n##\n')
for Author in AuthorDataset:
	infos = Author.split('\n\n')
	try:
		AuthorName,AuthorID = infos[0].split(' : ')
		LTE2005.append(infos[0]+'\n')
		G2005.append(infos[0]+'\n')
		for paper in infos[1:]:
			try:
				year = int(paper.split('\n')[1].replace(' : ',''))
				if year>2005:
					G2005.append(paper+'\n\n')
				else:
					LTE2005.append(paper+'\n\n')
			except:
				print "Exception : Year coming out to be", paper.split('\n')[1].replace(' : ','')
				# print paper
			
	except Exception, e:
		print "Except in", infos
		print '\n', e, '\n'
	G2005.append('\n\n##\n')
	LTE2005.append('\n\n##\n')
print 'Datasets Created'
with open('authors_till_2005.txt','w') as File:
	File.write(''.join(LTE2005))
with open('authors_after_2005.txt','w') as File:
	File.write(''.join(G2005))