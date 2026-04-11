from manim import BLUE, Scene, Text

from utility.mobjects.stick_figure import Expression, StickFigure


class CommitToYouArtwork(Scene):
    def construct(self):
        self.camera.background_color = BLUE
        stick_figure = StickFigure()

        initial_expression = Text(stick_figure.expression.value)
        self.add(stick_figure, initial_expression)
        self.play(stick_figure.set_and_animate_expression(Expression.NEUTRAL))
        new_expression = Text(stick_figure.expression.value)
        self.remove(initial_expression)
        self.add(new_expression)
        self.wait(2)
