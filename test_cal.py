from calc import add,sub,mul,div
import pytest

def test_add():
    assert add(2,5)==7

def test_sub(a,b):
     assert sub(5,3)==2

def test_mul(a,b):
     assert mul(2,5)==10

def test_div(a,b):
     assert div(15,5)==0