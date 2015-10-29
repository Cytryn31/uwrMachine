import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import SVM.classifySVM as cSVM
import Data.prep_terrain_data as prep_terrain_data
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.externals import joblib

features_train, labels_train, features_test, labels_test = prep_terrain_data.makeTerrainData()

# fit the model

clf = cSVM.getLinearSupportVectorClassifier()
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
#acc = accuracy_score(pred, labels_test)
#print (" accuracy: ", acc)

print(classification_report(labels_test, pred))
#precision = precision_score(labels_test, pred)
#print (" precision: ", precision)

#recall = recall_score(labels_test, pred)
#print (" recall: ", recall)

#f1 = f1_score(labels_test, pred)
#print (" f1: ", f1)

import pickle
s = pickle.dumps(clf)
print (" dumps: ", s)
print (" len: ", len(s))
clf2 = pickle.loads(s)

print(classification_report(labels_test, clf2.predict(features_test)))