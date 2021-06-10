import colorsys


class QualityPredictor:
    color_min_delta = 0.05
    color_max_delta = 0.2
    saturation_max_delta = 0.01
    value_max_delta = 0.15
    light_threshold = 0.6

    def predict(self, color1, color2):
        color1_hsv = colorsys.rgb_to_hsv(color1.r / 255, color1.g / 255, color1.b / 255)
        color2_hsv = colorsys.rgb_to_hsv(color2.r / 255, color2.g / 255, color2.b / 255)
        color1_hls = colorsys.rgb_to_hls(color1.r / 255, color1.g / 255, color1.b / 255)
        color2_hls = colorsys.rgb_to_hls(color2.r / 255, color2.g / 255, color2.b / 255)

        return self.color_min_delta < abs(color1_hsv[0] - color2_hsv[0]) < self.color_max_delta \
            and abs(color1_hsv[1] - color2_hsv[1]) < self.saturation_max_delta \
            and abs(color1_hsv[2] - color2_hsv[2]) < self.value_max_delta \
            and (color1_hls[1] + color2_hls[1]) / 2 > self.light_threshold
