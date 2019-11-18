

class Entity(object):
    def __init__(self):
        super(Entity, self).__init__()
        self.bbox = list
        self.label = str
        self.prob = 0.0

    def set_entity(self, bbox, label, prob):
        self.bbox = list(bbox)
        self.label = str(label)
        self.prob = prob
        return self
