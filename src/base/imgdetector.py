from luminoth import Detector, read_image, vis_objects
from config import BaseConfig
from src.entities.entity import Entity


class ImgDetector(object):
    def __init__(self):
        super(ImgDetector, self).__init__()
        self.detector = Detector()

    def predict_img(self, image_path: str) -> list:
        image_ = self.read_the_image(image_path)
        objects = self.detector.predict(image_)
        self.visual_objects(image_, objects)
        return objects

    @staticmethod
    def visual_objects(image, objects):
        vis_objects(image, objects).save(BaseConfig.IMAGE_OUTPUT)

    @staticmethod
    def read_the_image(image):
        image_ = read_image(image)
        return image_

    @staticmethod
    def find_object(objects: list, obj_label: str):
        global ent
        for item in objects:
            if item["label"] == obj_label:
                ent = Entity().set_entity(item["bbox"], item["label"], item["prob"])
        if ent.label == obj_label:
            return ent, True
        else:
            return None, False

