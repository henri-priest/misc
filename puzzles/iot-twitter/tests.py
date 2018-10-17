from main import dummy_function

""" This is to showcase basic usage of python unit tests. """

def test1():
    assert dummy_function(2, 2) == 4

def test2():
    assert dummy_function(2, 2) != -4

def test3():
    assert dummy_function(0, 2) == 0

def test4():
    assert dummy_function(1, 2) == 1
