import csv
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
 
clf = LinearSVC()

clf = joblib.load('svm.pkl') 

print clf.coef_
print clf.intercept_

print float(clf.predict([[13.5,22]]))/1000
