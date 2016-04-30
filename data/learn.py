import csv
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
 
samples_in = []
features_in = []
test = []
for i in xrange(1, 6): 
    with open('Anlage' + str(i) + '.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        count = 0
        for row in reader: 
            if reader.line_num == 1:
                continue
            if count % 10 is 0:
                test.append([row[1],row[2],row[3]])
                count += 1
                continue
            samples_in.append(int(float(row[3])*1000))
        
            feature = []
            feature.append(float(row[1]))
            feature.append(float(row[2]))
            features_in.append(feature)
            count += 1

samples = np.array(samples_in)
features = np.array(features_in)

print features
print samples
print test
f = open('test_data.txt', 'w')
f.write(str(test))
f.close()

clf = LinearSVC()

clf = clf.fit(features, samples)

joblib.dump(clf, 'svm_new.pkl')

print clf.coef_
print clf.intercept_
