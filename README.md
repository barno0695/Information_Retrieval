# Information_Retrieval
Term project involving recommending researchers to other researchers keeping their diversity in mind

Progress:   Total no. of authors now = 11143... Shortlisted the ones who have > 31 papers till 2005 and > 5 papers after 2005
			We have diversity of any two authors as a matrix stored in 'cosine_distances_fields.npy' file.
			We have created the datasets i.e. for each author, we have some authors who worked with him after 2005 which are:
				1. Diverse (cosine similarity <= 0.2) - in diverse_coauthors.p
				2. Similar (cosine similarity > 0.2)  - in similar_coauthors.p
			We wrote the code to find the fields of citations of every paper in a dictionary 'citation_field_vectors.p' but citation network info that we have seems unadequete/different to be meaningful. I thought we should go by grepping '#index|#%f' in all papers data but even that can not be done since dumped_data_all_authors does not have lines starting from '#%f' (No field information for citations in the dataset)... May be we have to drop this feature.
			Some code has been written for LDA training but is basically unupdated
			

#Run the following commands to set up the system #######################################

#First clone this repo to your local machine if you have not done so. 'duhh!!'
#The command for cloning is - "git clone https://github.com/priyankpalod/Information_Retrieval.git
#If that gives error, maybe you don't have git installed on your machine. Run 'sudo apt-get install git' and retry 
#Upon successful cloning, run 'cd Information_Retrieval' and continue with the commands below (without the quotes, of course!)


"scp 13CS10037@10.5.18.104:./Information_Retrieval/dumped_data_all_papers . "				# Copies the 17GB file... will take some time
"scp 13CS10037@10.5.18.104:./Information_Retrieval/dumped_data_authors.txt . "				# Another file copy
"grep -E '#index|^#f' dumped_data_all_papers > fieldsData.txt"  	# Creates the fieldsData.txt file by a simple grep. May take some time
"python system.py" 													# Will take up a lot of time... do not worry.. just a one time command :)
