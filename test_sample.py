import pytest
from utils import make_param_combinations

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