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
from utils import preprocess_data, make_param_combinations, read_digits,predict_and_eval,train_test_dev_split, tune_hparams


gamma_ranges = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
C_ranges = [0.1,1,2,5,10]
param_list_dict = {'gamma':gamma_ranges,'C':C_ranges}

test_size_ranges = [0.1, 0.2, 0.3]
dev_size_ranges = [0.1, 0.2, 0.3]
split_size_list_dict = {'test_size':test_size_ranges,'dev_size':dev_size_ranges}

# Read digits: Create a classifier: a support vector classifier
x_digits,y_digits = read_digits()

#Find best model for given gamma and C range

splits = make_param_combinations(split_size_list_dict)

for split in splits:

    # Data splitting: Split data into train, test and dev as per given test and dev sizes
    X_train, X_test, X_dev, y_train, y_test, y_dev = train_test_dev_split(x_digits,y_digits, **split)

    # Data preprocessing
    X_train = preprocess_data(X_train)
    X_test = preprocess_data(X_test)
    X_dev = preprocess_data(X_dev)

    best_hparams,best_model, best_accuracy =  tune_hparams(X_train,y_train,X_dev,y_dev,param_list_dict)

    _,train_acc = predict_and_eval(best_model,X_train,y_train,c_report=False,c_matrix=False)
    _,test_acc = predict_and_eval(best_model,X_test,y_test,c_report=False,c_matrix=False)
    _,dev_acc = predict_and_eval(best_model,X_dev,y_dev,c_report=False,c_matrix=False)

    print("Test size=%g, Dev size=%g, Train_size=%g, Train_acc=%.4f, Test_acc=%.4f, Dev_acc=%.4f" % (split['test_size'],split['dev_size'],1-split['test_size']-split['dev_size'],train_acc,test_acc,dev_acc) ,sep='')
    print("Best hparams:= ",dict([(x,best_hparams[x]) for x in param_list_dict.keys()]))

    # Getting model predictions on test set
    # Predict the value of the digit on the test subset

    # predicted,best_accuracy = predict_and_eval(best_model,X_test,y_test,c_report=False,c_matrix=False)
    # print("Test Accuracy:",best_accuracy)

