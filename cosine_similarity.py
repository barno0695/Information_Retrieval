import math
import numpy
import heapq
# # File containing Topic Names and there corresponding count
# vector_file_researcher_1 = open("researcher_file_1.txt","r")
# vector1 = vector_file_researcher_1.readline()
# vector_file_researcher_2 = open("researcher_file_2.txt","r")
# vector2 = vector_file_researcher_2.readline()


def cosine_simlarity(vector1,vector2):
	sum = 0
	norm1 = 0.0
	norm2 = 0.0

	for element1,element2 in zip(vector1,vector2):
	    sum = sum + element1*element2
	    norm1 = norm1 + element1 * element1
	    norm2 = norm2 + element2 * element2     


	norm1 = math.sqrt(norm1)
	norm2 = math.sqrt(norm2)

	ans = sum/(norm1*norm2)

	return ans

def loadVectors(filename):
	dictionary = {}
	IdtoPosition = {}
	with open(filename,'r') as VectorsFile:
		VectorsFile = VectorsFile.read()
	authors = VectorsFile.split('\n\n')
	pos = 0;
	for author in authors:
		try:
			author_details,vector = author.split('\n')
		except:
			print author
		Id = int(author_details.split(' : ')[1])
		IdtoPosition[Id] = pos
		pos += 1
		dictionary[Id] = [int(val) for val in vector.strip().split(' ')]
	return dictionary,IdtoPosition


NumberOfTopDistancesToKeep = 100

IdtoVector, IdtoPosition = loadVectors('field_frequency_vector.txt')
print 'size of matrix = ',len(IdtoVector)
matrix = numpy.zeros((len(IdtoVector),NumberOfTopDistancesToKeep)
for Id1 in IdtoVector:
	for Id2 in IdtoVector:
		sim = cosine_simlarity(IdtoVector[Id1],IdtoVector[Id2])
		matrix[IdtoPosition[Id1]][IdtoPosition[Id2]] = sim
	print 'row done'