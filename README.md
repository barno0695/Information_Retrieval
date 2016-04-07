# Researcher Recommendation System
Term project involving recommending researchers to other researchers keeping their diversity in mind


**Progress**:   

Total no. of authors now = 11143... Shortlisted the ones who have > 31 papers till 2005 and > 5 papers after 2005

			
We have diversity of any two authors as a matrix stored in '*cosine_distances_fields.npy*' file.

			
We have created the datasets i.e. for each author, we have some authors who worked with him after 2005 which are:

- Diverse (cosine similarity <= 0.2) - in *diverse_coauthors.p*
- Similar (cosine similarity > 0.2)  - in *similar_coauthors.p*


We wrote the code to find the fields of citations of every paper in a dictionary '*citation_field_vectors.p*' but citation network info that we have seems unadequete/different to be meaningful. 

I thought we should go by grepping '*#index|#%f*' in all papers data but even that can not be done since *dumped_data_all_authors* does not have lines starting from '*#%f*' (No field information for citations in the dataset)... May be we have to drop this feature.

Some code has been written for LDA training but is basically still not updated.
			

**Run the following commands to set up the system**

First clone this repo to your local machine if you have not done so. 'duhh!!'

The command for cloning is - 
> git clone https://github.com/priyankpalod/Information_Retrieval.git

If that gives error, maybe you don't have git installed on your machine. Try installing git and retry
> sudo apt-get install git

Upon successful cloning, enter the repository directory and continue with the commands mentioned below

- To copy the 17GB papers file, run the following command in your terminal. This may take some time depending on your internet speed.
> scp 13CS10037@10.5.18.104:./Information_Retrieval/dumped_data_all_papers .

- To copy the authors file, run the following command in your terminal.				
> scp 13CS10037@10.5.18.104:./Information_Retrieval/dumped_data_authors.txt .

- To create the fieldsData.txt file by a simple grep, run this command. May take some time.
> grep -E '#index|^#f' dumped_data_all_papers > fieldsData.txt

- This will take up a lot of time... do not worry.. just a one time command :)
> python system.py 													
