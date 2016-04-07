# Author - Priyank Palod
try:
	import cPickle as pickle
except:
	import pickle
coauthors = {}
papersToAuthors = {}
authorsData = ''

def makePapersToAuthors():
	global authorsData
	global papersToAuthors
	authorsDataList = authorsData.split('\n\n##\n')[:-1]
	for author in authorsDataList:
		infos = author.split('\n\n')
		try:
			AuthorID = int(infos[0].split(' : ')[1])
			for paper in infos[1:-1]:
				try:
					paperId = int(paper.split('\n')[0])
					try:
						papersToAuthors[paperId].append(AuthorID)
					except:
						papersToAuthors[paperId] = [AuthorID]
				except:
					print "Exception : paperId coming out to be",paper.split('\n')[0]
					print infos
		except Exception, e:
			print "Except : AuthorID coming out to be", infos[0].split(' : ')[1]
			print '\n', e, '\n'

def makeCoAuthors():
	global papersToAuthors
	global coauthors
	for paper in papersToAuthors:
		authors = papersToAuthors[paper]
		for author in authors:
			for coauthor in authors:
				if author == coauthor:
					continue
				else:
					try:
						coauthors[author].append(coauthor)
					except:
						coauthors[author] = [coauthor]

### starting from scratch ###
def startFromScratch():
	global papersToAuthors
	global coauthors
	global authorsData
	filename = 'authors_after_2005.txt'
	with open(filename,'r') as authorsFile:
		authorsData = authorsFile.read()
	print 'File read'

	makePapersToAuthors()
	pickle.dump(papersToAuthors,open('papersToAuthorsAfter2005.p','wb'))
	print 'Making coauthors'
	makeCoAuthors()
	print 'dumping coauthors'
	pickle.dump(coauthors,open('coauthorsAfter2005.p','wb'))