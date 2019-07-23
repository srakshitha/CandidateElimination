import numpy as np
import csv

data = []
reader = csv.reader(open('.\CandidateElimination_train.csv', 'r'), delimiter = ',')
for row in reader: data.append(np.array(row))

data = np.asarray(data, dtype = 'object') 
X = data[:, :-1]
Y = data[:, -1].reshape(X.shape[0], 1) 

specificH = [" % " for _ in range(X.shape[1])]
specificH = np.asarray(specificH, dtype = 'object')
generalH = [[" ? " for _ in range(X.shape[1])] for _ in range(X.shape[1])]
generalH = np.asarray(generalH, dtype = 'object')

if Y[0] == "Yes":
    specificH = X[0]
else:
    for i in range(Y.shape[0]):
        if Y[i] == "Yes":
            specificH = X[i]
            break

for i in range(X.shape[0]):
    if Y[i] == "Yes":
        for j in range(X.shape[1]):
            if X[i][j] != specificH[j]:
                specificH[j] = '?'
            if specificH[j] != generalH[j][j] and generalH[j][j] != "?":
                generalH[j][j] = "?"   
    else:
        for j in range(X.shape[1]):
            if X[i][j] != specificH[j]:
                generalH[j][j] = specificH[j]

print ("\nFinal Specific Hypothesis : ")
print (specificH)
print ("\nFinal General Hypothesis : ")
print (generalH)