import pytest

from mypackage import datahub

def test_data_folder(debug_mode):
    fd = datahub.FDATA
    assert fd.exists()
