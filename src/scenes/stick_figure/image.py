from manim import BLUE, Scene, config

from utility.mobjects.stick_figure import StickFigure


class StickFigureImage(Scene):
    def construct(self):
        config.pixel_width = 3000
        config.pixel_height = 3000

        self.camera.background_color = BLUE
        stick_figure = StickFigure()

        self.add(stick_figure)
