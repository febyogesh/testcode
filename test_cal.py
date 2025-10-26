from calc import add,sub,mul,div
import pytest

def test_add():
    assert add(2,5)==7

def test_sub():
     assert sub(5,3)==2

def test_mul():
     assert mul(2,5)==10

def test_div():
     assert div(15,5)==3