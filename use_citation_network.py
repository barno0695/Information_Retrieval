# Author - Priyank Palod
'''
Problems : Most of the papers in the dataset are not present in the citation_network
'''


try:
	import cPickle as pickle
except:
	import pickle
citation_network = {}

def load():
	'''
	This function basically gives a dictionary for paper:[list of papers it cited]
	'''
	global citation_network
	linesDone = 0
	for line in open('citation_network_new','r'):
		paperId, citation = line.split('\t')
		# print paperId,citation
		try:
			paperId = int(paperId)
			citation = int(citation)
		except:
			continue
		try:
			citation_network[paperId].append(citation)
		except:
			citation_network[paperId] = [citation]
		linesDone+=1
		if((linesDone&262143)==0):
			print linesDone

field_index = {
	'scientific_computing': 0, 
	'information_retrieval': 1, 
	'world_wide_web': 2, 
	'security_and_privacy': 3, 
	'computer_education': 4, 
	'distributed_and_parallel_computing': 5, 
	'programming_languages': 6, 
	'algorithms_and_theory': 7, 
	'networks_and_communications': 8, 
	'machine_learning_and_pattern_recognition': 9, 
	'multimedia': 10, 
	'databases_': 11, 
	'human_computer_interaction': 12, 
	'natural_language_and_speech': 13, 
	'artificial_intelligence': 14, 
	'real_time_and_embedded_systems': 15, 
	'bioinformatics_and_computational_biology': 16, 
	'hardware_and_architecture': 17, 
	'data_mining': 18, 
	'graphics': 19, 
	'software_engineering': 20, 
	'computer_vision': 21, 
	'simulation': 22, 
	'operating_systems': 23
}

vectors = {}
citation_vectors = {}

def getFields():
	'''
	This function gives us the fields for every paper
	'''
	global vectors
	global citation_network
	with open('fieldsData.txt','r') as f:
		pairsDone = 0
		for line in f:
			if '#index' in line:
				paperId = int(line.replace('#index',''))
			else:
				fieldNum = field_index[line.replace('#f','').strip('\n')]
				try:
					vectors[paperId][fieldNum]+=1
					if paperId == 50331658:
						print 'paperId = 50331658 ', vectors[paperId][fieldNum]
				except:
					vectors[paperId] = [0]*24
					vectors[paperId][fieldNum]+=1
			pairsDone+=1
			if((pairsDone&262143)==0):
				print pairsDone

def getCitationFieldVectorsForPaper():
	'''
	This function should give us the fields of all the papers a paper has cited 
	'''
	global vectors
	global citation_network
	global citation_vectors
	papersDone = 0
	errors = ''
	for paperId in vectors:
		citation_vectors[paperId] = [0]*24
		try:
			for citedPaper in citation_network[paperId]:
				citation_vectors[paperId] = [sum(x) for x in zip(citation_vectors[paperId],vectors[citedPaper])]
		except:
			errors+="Citations info not available for\t"+str(paperId)+"\n"
		papersDone+=1
		if((papersDone&262143)==0):
			print papersDone
	with open('CitationsNotAvailable.txt','w') as Errorfile:
		Errorfile.write(errors)

def startFromScratch():
	global vectors
	global citation_network
	global citation_vectors
	load()
	print 'Loaded'
	pickle.dump(citation_network,open("citation_network.p","wb"))
	print 'dumped'
	getFields()
	print 'Got Fields'
	pickle.dump(vectors,open("field_vectors.p","wb"))
	print 'dumped field vectors'
	getCitationFieldVectorsForPaper()
	print 'Got citation fields'
	pickle.dump(citation_vectors,open("citation_field_vectors.p","wb"))
	print 'dumped citation_vectors'
	for paperId in citation_vectors:
		print paperId, ":", citation_vectors[paperId]

startFromScratch()
# citation_network = pickle.load(open("citation_field_vectors.p","rb"))