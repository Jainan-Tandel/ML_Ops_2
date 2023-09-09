"""
================================
Recognizing hand-written digits
================================

This example shows how scikit-learn can be used to recognize images of
hand-written digits, from 0-9.

"""

# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause

# Import datasets, classifiers and performance metrics
from sklearn import metrics
from utils import preprocess_data, split_data, train_model, read_digits,predict_and_eval,train_test_dev_split, tune_hparams


gamma_ranges = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
C_ranges = [0.1,1,2,5,10]
param_list_dict = {'gamma':gamma_ranges,'C':C_ranges}

# Read digits: Create a classifier: a support vector classifier
x,y = read_digits()

# Data splitting: Split data into 70% train, 20% test and 10% dev subsets
X_train, X_test, X_dev, y_train, y_test, y_dev = train_test_dev_split(x,y, test_size=0.2,dev_size=0.1)

# Data preprocessing
X_train = preprocess_data(X_train)
X_test = preprocess_data(X_test)
X_dev = preprocess_data(X_dev)

#Find best model for given gamma and C range

best_hparams,best_model, best_accuracy =  tune_hparams(X_train,y_train,X_dev,y_dev,param_list_dict)

print("Best hparams:")
for x in param_list_dict.keys(): print(x,best_hparams.get(x)) 

# Getting model predictions on test set
# Predict the value of the digit on the test subset

predicted,best_accuracy = predict_and_eval(best_model,X_test,y_test)
print("Test Accuracy:",best_accuracy)

