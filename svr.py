from sklearn.svm import SVR

Y = []
X = []
Z = []
clf = SVR(C=1.0, epsilon=0.002)

def train():
	with open("train") as f:
		for line in f:
			lines = line.split()
			X.append(lines[0:-1])
			Y.append(lines[-1]) 

	print X
	print Y

	# clf = svm.SVC()
	clf.fit(X,Y)


	with open("test") as f:
		for line in f:
			lines = line.split()
			Z.append(lines)

	op = clf.predict(Z)
	print op

train()