from manim import RIGHT, WHITE, Line, Rectangle, VGroup


class AlexUpBotMouth(VGroup):
    def __init__(self, *vmobjects, **kwargs):
        super().__init__(*vmobjects, **kwargs)
        underscore = Rectangle(
            width=0.6,
            height=0.08,
            color=WHITE,
        ).set_fill("#30363d", opacity=1)

        arrow_top = Line(
            start=[-0.1, 0.15, 0],
            end=[0.15, 0.0, 0],
            color=WHITE,
        )

        arrow_bottom = Line(
            start=[-0.1, -0.15, 0],
            end=[0.15, 0.0, 0],
            color=WHITE,
        )
        arrow = VGroup(arrow_top, arrow_bottom)

        self.add(arrow, underscore)
        self.arrange(RIGHT, buff=0.1)
