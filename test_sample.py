import pytest
import numpy as np  
from utils import make_param_combinations, train_test_dev_split, read_digits

# def inc(x):
#     return x+1

# def test_answer():
#     assert inc(3)==5

# def test_wrong_answer():
#     assert not inc(3)==5

def test_hparam_combinations():
    params = {'gamma':[0.001,0.1],'C':[1,10]}
    h_param_combinations = make_param_combinations(params)
    assert ({'gamma':0.001,'C':1} in h_param_combinations) and ({'gamma':0.1,'C':1} in h_param_combinations) and ({'gamma':0.001,'C':10} in h_param_combinations) and ({'gamma':0.1,'C':10} in h_param_combinations)

def test_split():
    X = np.linspace(0,1,100)
    y = np.linspace(0,1,100)
    split = {'test_size':0.1,'dev_size':0.6}
    X_train, X_test, X_dev, y_train, y_test, y_dev = train_test_dev_split(X,y, **split)
    assert len(X_train)==30 and len(X_test)==10 and len(X_dev)==60

