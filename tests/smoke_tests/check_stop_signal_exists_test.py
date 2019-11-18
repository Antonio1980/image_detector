import allure
import pytest
from config import BaseConfig
from src.base import logger
from src.base.log_decorator import automation_logger


@allure.feature("Label")
@pytest.mark.usefixtures("img_detector")
class TestStopSignal(object):

    @allure.testcase("", name="Stop Signal")
    @automation_logger(logger)
    def test_that_stop_signal_exist(self, img_detector):
        obj_ = img_detector.predict_img(BaseConfig.IMAGE_INPUT)
        entity_, assert_ = img_detector.find_object(obj_, obj_label='stop sign')
        assert entity_ is not None and assert_ is True
        logger.logger.info("Test is passed!")
