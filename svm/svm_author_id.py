#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import svm
from sklearn.metrics import accuracy_score

clf = svm.SVC(kernel='rbf', C=10000)

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print "training time: ", round(time()-t0, 3), "s"
pred = clf.predict(features_test)
accuracy = accuracy_score(pred, labels_test)

count = 0
for i in range(len(pred)):
	if pred[i]==1:	# if email is sent by Chris
		count+=1

print count

a1 = pred[10]
a2 = pred[26]
a3 = pred[50]

print a1, " ", a2, " ", a3

print "Accuracy: ", accuracy


#########################################################


