import math
import numpy
try:
	import cPickle as pickle
except:
	import pickle

def cosine_simlarity(vector1,vector2):
	sumx = 0
	norm1 = 0.0
	norm2 = 0.0

	for element1,element2 in zip(vector1,vector2):
	    sumx = sumx + element1*element2
	    norm1 = norm1 + element1 * element1
	    norm2 = norm2 + element2 * element2     


	norm1 = math.sqrt(norm1)
	norm2 = math.sqrt(norm2)

	if norm1==0 or norm2==0:
		ans = 0
	else:
		ans = sumx/(norm1*norm2)

	return ans

def loadVectors(filename):
	dictionary = {}
	IdtoPosition = {}
	with open(filename,'r') as VectorsFile:
		VectorsFile = VectorsFile.read()
	authors = VectorsFile.split('\n\n')[:-1]
	pos = 0;
	for author in authors:
		try:
			author_details,vector = author.split('\n')
		except:
			print author
		Id = int(author_details.split(' : ')[1])
		IdtoPosition[Id] = pos
		pos += 1
		print IdtoPosition[Id]
		dictionary[Id] = [int(val) for val in vector.strip().split(' ')]
	return dictionary,IdtoPosition


def startFromScratch():
	IdtoVector, IdtoPosition = loadVectors('field_frequency_vector.txt')
	print 'size of matrix = ',len(IdtoVector)
	i = 0
	matrix = numpy.zeros((len(IdtoVector),len(IdtoVector)))
	for Id1 in IdtoVector:
		for Id2 in IdtoVector:
			sim = cosine_simlarity(IdtoVector[Id1],IdtoVector[Id2])
			matrix[IdtoPosition[Id1]][IdtoPosition[Id2]] = sim
		print 'row done', i
		i+=1
	pickle.dump(IdtoPosition,open('IdtoMatrixPositionAuthors.p','wb'))
	numpy.save('cosine_distances_fields',matrix)