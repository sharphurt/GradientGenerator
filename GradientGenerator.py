from PIL import Image


class GradientGenerator:
    def __init__(self, size):
        self.img = Image.new('RGB', size, "black")
        self.pixels = self.img.load()

    def generate(self, colors):
        pass
