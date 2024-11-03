from ._base import Structure

class Carvalho(Structure):
    def __init__(self, position, sprite = "assets/Tree.png", size = (200,240)):
        super().__init__(sprite, size, position, rect_height= 2)
        