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

with open('reduced_authors.txt','r') as AuthorDataset:
	AuthorDataset = AuthorDataset.read()
print "File read"
LTE2005 = []
AuthorDataset = AuthorDataset.split('\n\n##\n')
for Author in AuthorDataset:
	count_variable = [0]*24
	infos = Author.split('\n\n')
	try:
		AuthorName,AuthorID = infos[0].split(' : ')
		LTE2005.append(infos[0]+'\n')
		for paper in infos[1:]:
			try:
				year = int(paper.split('\n')[1].replace(' : ',''))
				if year<=2005:
					field_name = paper.split('\n')[2].split()[1]
					if(AuthorName=='Alexandros Agapitos' and field_name=='artificial_intelligence'):
						print "Yo"
					count_variable[field_index[field_name.strip()]]+=1
			except:
				print "Exception : Year coming out to be", paper.split('\n')[1].replace(' : ','')
	except Exception, e:
		print "Except in", infos
		print '\n', e, '\n'
	for i in count_variable:
		LTE2005.append(str(i)+' ')
	LTE2005.append('\n\n')
print 'Datasets Created'
with open('field_frequency_vector.txt','w') as File:
	File.write(''.join(LTE2005))