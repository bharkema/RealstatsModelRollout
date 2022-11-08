import pytest
import RealstatsModelRollout as RMR
from .settings import settings

def test_save_validation():
    validation = RMR.Validate()
    RMR.Settings.Gitaccesstoken = settings.Gitaccesstoken

    validation.Mae_expected_value = 200
    validation.MAE_Deviation_percentage = 5
    validation.R2_expected_value = 90
    validation.R2_Deviation_percentage = 2

    validation.Save_validation_results("c:/")























