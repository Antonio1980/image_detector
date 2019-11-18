import os
import allure
import pytest
from config import BaseConfig
from src.base import logger
from src.base.log_decorator import automation_logger


@allure.feature("Label")
@pytest.mark.usefixtures("img_detector")
class TestHowManyCars(object):

    @allure.testcase("test_how_many_cars_exist", name="")
    @automation_logger(logger)
    def test_how_many_cars_exist(self, img_detector):
        print("------------------------------" + BaseConfig.IMAGE_INPUT + "------------------------")
        obj_ = img_detector.predict_img(BaseConfig.IMAGE_INPUT)
        filtered_obj = [i for i in obj_ if i["label"] == "car"]
        assert len(filtered_obj) >= 8
        logger.logger.info("Test is passed!")
