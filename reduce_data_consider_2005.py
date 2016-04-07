# Author - Priyank Palod
def main():
	with open('dumped_data_authors.txt','r') as AuthorDataset:
		AuthorDataset = AuthorDataset.read()
	print "File read"
	LTE2005 = []
	G2005 = []
	reduced_authors = []
	AuthorDataset = AuthorDataset.split('\n\n##\n')
	print 'initially authors = ',len(AuthorDataset)
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
						G2005.append(paper)
					else:
						LTE2005.append(paper)
				except:
					# print "Exception : Year coming out to be", paper.split('\n')[1].replace(' : ','')
					G2005 = []
					break
					# print paper
				
		except Exception, e:
			print "Except in", infos
			print '\n', e, '\n'
		if len(G2005)>5 and len(LTE2005)>31:
			reduced_authors.append(Author + '\n\n##\n')
		G2005 = []
		LTE2005 = []
	print 'Datasets Created with no. of authors=', len(reduced_authors)
	with open('reduced_authors.txt','w') as File:
		File.write(''.join(reduced_authors))
