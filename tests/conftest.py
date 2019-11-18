import pytest
from src.base.imgdetector import ImgDetector


@pytest.fixture(scope="class")
def img_detector():
    return ImgDetector()
