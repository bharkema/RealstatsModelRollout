import pytest
import RealstatsModelRollout as RMR

def test_Find_correct():
    assert RMR.globalFunctions.Find("test/string", "/") == [4]

def test_Find_incorrect():
    assert RMR.globalFunctions.Find("test/string", "/") != [2]

def test_Path_correct():
    assert RMR.globalFunctions.Path_is_dir("c:/") == "c:/"
