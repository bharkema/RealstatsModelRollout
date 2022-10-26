import pytest
import RealstatsModelRollout as RMR
from .settings import settings

def test_Find_correct():
    assert RMR.globalFunctions.Find("test/string", "/") == [4]

def test_Find_incorrect():
    assert RMR.globalFunctions.Find("test/string", "/") != [2]

def test_Path_correct():
    assert RMR.globalFunctions.Path_is_dir(settings.Main_path) == settings.Main_path

def test_Path_incorrect():
    with pytest.raises(Exception) as exc:
        RMR.globalFunctions.Path_is_dir("c:/")
        assert "Given localpath: c:/ is not a directory" in str(exc.value)
