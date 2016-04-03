with open('dumped_data_authors.txt','r') as AuthorDataset:
	AuthorDataset = AuthorDataset.read()
print "File read"
THRESHHOLD = 11
FinalData = []
AuthorDataset = AuthorDataset.split('\n\n##\n')
count = 0
print 'initially authors = ',len(AuthorDataset)
for Author in AuthorDataset:
	infos = Author.split('\n\n')
	if len(infos)>THRESHHOLD:
		FinalData.append(Author)
		count+=1
		FinalData.append('\n\n##\n')
print 'Datasets Created no. of authors = ', count
with open('reduced_authors.txt','w') as File:
	File.write(''.join(FinalData))