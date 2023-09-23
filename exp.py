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
from skimage.transform import rescale, resize, downscale_local_mean
import numpy as np

# Read digits: Create a classifier: a support vector classifier
x,y = read_digits();


# Data splitting: Split data into 70% train, 20% test and 10% dev subsets
X_train, X_test, X_dev, y_train, y_test, y_dev = train_test_dev_split(x,y, test_size=0.2,dev_size=0.1)



print(f"The number of total samples in the dataset: {len(X_train)+len(X_test)+len(X_dev)}")
print(f"The shape of all images in the dataset: {X_train[0].shape}")


resize_range = [1,0.75,0.5]
for resize_size in resize_range:
    new_x = []
    for image in X_train:
        image_resized = rescale(image, resize_size, anti_aliasing=False)
        new_x.append(image_resized)
    x = np.array(new_x)

    new_x_test = []
    for image in X_test:
        image_resized = rescale(image, resize_size, anti_aliasing=False)
        new_x_test.append(image_resized)
    x_test = np.array(new_x_test)

    new_x_dev = []
    for image in X_dev:
        image_resized = rescale(image, resize_size, anti_aliasing=False)
        new_x_dev.append(image_resized)
    x_dev = np.array(new_x_dev)

    # Data preprocessing
    X_train = preprocess_data(x)
    X_test = preprocess_data(x_test)
    X_dev = preprocess_data(x_dev)

    #Model training
    model = train_model(X_train, y_train,{'gamma':0.001},model_type="svm")

    # Getting model predictions on test set
    # Predict the value of the digit on the test subset
    print(f"Resize size: {resize_size}")
    print(f"Test")
    predicted = predict_and_eval(model,X_test,y_test,c_matrix=False,c_report=False)
    print(f"Dev")
    predicted_dev = predict_and_eval(model,X_dev,y_dev,c_matrix=False,c_report=False)

