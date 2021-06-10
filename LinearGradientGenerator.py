from GradientGenerator import GradientGenerator


class LinearGradientGenerator(GradientGenerator):
    def generate(self, colors):
        for x in range(self.img.size[0]):
            for y in range(self.img.size[1]):
                self.pixels[x, y] = (
                    int(colors[0].r * (100 / self.img.size[0] * x) / 100 + colors[1].r * (
                            1 - ((100 / self.img.size[0] * x) / 100))),
                    int(colors[0].g * (100 / self.img.size[0] * x) / 100 + colors[1].g * (
                            1 - ((100 / self.img.size[0] * x) / 100))),
                    int(colors[0].b * (100 / self.img.size[0] * x) / 100 + colors[1].b * (
                            1 - ((100 / self.img.size[0] * x) / 100))),
                )

        return self.img
