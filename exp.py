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
from utils import preprocess_data, split_data, train_model, read_digits,predict_and_eval,train_test_dev_split

gamma_ranges = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
C_ranges = [0.1,1,2,5,10]

# Read digits: Create a classifier: a support vector classifier
x,y = read_digits();

# Data splitting: Split data into 70% train, 20% test and 10% dev subsets
X_train, X_test, X_dev, y_train, y_test, y_dev = train_test_dev_split(x,y, test_size=0.2,dev_size=0.1)

# Data preprocessing
X_train = preprocess_data(X_train)
X_test = preprocess_data(X_test)
X_dev = preprocess_data(X_dev)

#Find best model for given gamma and C range

best_accuracy_so_far = -1
best_model = None
for cur_gamma in gamma_ranges:
    for cur_c in C_ranges:
        cur_model = train_model(X_train, y_train, {'gamma': cur_gamma,'C':cur_c}, model_type='svm')
        predicted, cur_accuracy = predict_and_eval(cur_model, X_dev, y_dev,c_report=False,c_matrix=False)
        if cur_accuracy > best_accuracy_so_far:
            print("New best accuracy:",cur_accuracy)
            best_accuracy_so_far = cur_accuracy
            optimal_gamma = cur_gamma
            optimal_C = cur_c
            best_model = cur_model

print("Optimal C:",optimal_C, "& Optimal gamma:", optimal_gamma)


# Getting model predictions on test set
# Predict the value of the digit on the test subset

predicted,best_accuracy = predict_and_eval(best_model,X_test,y_test)
print("Test Accuracy:",best_accuracy)

