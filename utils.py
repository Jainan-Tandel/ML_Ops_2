from sklearn import datasets, metrics, svm
from sklearn.model_selection import train_test_split

def read_digits():
    digits = datasets.load_digits()
    x = digits.images
    y = digits.target
    return x,y

def split_data(x,y, test_size, shuffle = False, random_state = 42):
    X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.5, shuffle=False)
    return X_train, X_test, y_train, y_test

def preprocess_data(data):
    n_samples = len(data)
    data = data.reshape((n_samples, -1))
    return data
    
def train_model(x,y,model_params,model_type="svm"):
    if model_type == "svm":
        clf = svm.SVC
    model = clf(**model_params)
    model.fit(x,y)
    return model