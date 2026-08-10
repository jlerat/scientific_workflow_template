from pathlib import Path
import pytest

from mypackage import datahub

from hydrodiy.io import iutils

from loggers import get_logger

FTEST = Path(__file__).resolve().parent

def test_data_folder(debug_mode):
    logger = get_logger(debug_mode)
    fd = datahub.FDATA
    assert fd.exists()
    logger.info("FDATA exists!")
