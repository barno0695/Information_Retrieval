# Author - Priyank Palod
'''
Can Vary threshold in makeDatasets function

To create datasets of -
	For each author, some authors which were diverse from it before 2005 but have worked with him after 2005
					 and some authors which are similar and worked after 2005
'''

import numpy
try:
	import cPickle as pickle
except:
	import pickle


def makeDatasets():
	Threshhold = 0.2
	cosine_similarity = numpy.load('cosine_distances_fields.npy')
	coauthors = pickle.load(open('coauthorsAfter2005.p','rb'))
	IdtoPosition = pickle.load(open('IdtoMatrixPositionAuthors.p','rb'))
	diverse = {}
	similar = {}
	for author in coauthors:
		diverse[author] = []
		similar[author] = []
		for coauthor in coauthors[author]:
			if cosine_similarity[IdtoPosition[author]][IdtoPosition[coauthor]] > Threshhold:
				diverse[author].append(coauthor)
			else:
				similar[author].append(coauthor)
		print len(diverse[author]), len(similar[author])
		if len(diverse[author])==0 or len(similar[author])==0:
			print 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'
	return diverse,similar

def startFromScratch():
	diverse,similar = makeDatasets()
	pickle.dump(diverse,open('diverse_coauthors.p','wb'))
	pickle.dump(similar,open('similar_coauthors.p','wb'))