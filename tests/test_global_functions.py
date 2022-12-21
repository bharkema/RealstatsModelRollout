import pytest
import RealstatsModelRollout as RMR
from .settings import settings

# Tests if function gives appropiate response
def test_Find_correct():
    assert RMR.globalFunctions.Find("test/string", "/") == [4]

# Tests if function gives appropiate response
def test_Find_incorrect():
    assert RMR.globalFunctions.Find("test/string", "/") != [2]

# Tests if function gives appropiate response
def test_Path_correct():
    assert RMR.globalFunctions.Path_is_dir(settings.Main_path) == settings.Main_path

# Tests if function gives appropiate response
def test_Path_incorrect():
    with pytest.raises(Exception) as exc:
        RMR.globalFunctions.Path_is_dir("c:/")
        assert "Given localpath: c:/ is not a directory" in str(exc.value)

# Tests if function gives appropiate response
def test_Check_instance_correct_string():
    RMR.globalFunctions.Check_instance("Hallo", "string")

# Tests if function gives appropiate response
def test_Check_instance_incorrect_string():
    with pytest.raises(Exception) as exc:
        RMR.globalFunctions.Check_instance([], "string")
        assert "Type is not string" in str(exc.value)

# Tests if function gives appropiate response
def test_Check_instance_correct_float():
    RMR.globalFunctions.Check_instance(4.222, "float")

# Tests if function gives appropiate response
def test_Check_instance_incorrect_float():
    with pytest.raises(Exception) as exc:
        RMR.globalFunctions.Check_instance("hallo", "float")
        assert "Type is not string" in str(exc.value)

# Tests if function gives appropiate response
def test_Check_instance_correct_int():
    RMR.globalFunctions.Check_instance(5, "int")

# Tests if function gives appropiate response
def test_Check_instance_incorrect_int():
    with pytest.raises(Exception) as exc:
        RMR.globalFunctions.Check_instance(4.2, "int")
        assert "Type is not string" in str(exc.value)

# Tests if function gives appropiate response
def test_Check_instance_correct_list():
    RMR.globalFunctions.Check_instance([], "list")

# Tests if function gives appropiate response
def test_Check_instance_incorrect_list():
    with pytest.raises(Exception) as exc:
        RMR.globalFunctions.Check_instance({}, "list")
        assert "Type is not string" in str(exc.value)
