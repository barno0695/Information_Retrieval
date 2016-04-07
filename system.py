# Author - Priyank Palod
###### Just run this :)###########

import reduce_data_consider_2005
import seperate_yearwise
import frequency_vector
import cosine_similarity
import make_coauthors
import create_datasets

def initialize_system():
	reduce_data_consider_2005.main()
	seperate_yearwise.main()
	frequency_vector.startFromScratch()
	cosine_similarity.startFromScratch()
	make_coauthors.startFromScratch()
	create_datasets.startFromScratch()
	
initialize_system()