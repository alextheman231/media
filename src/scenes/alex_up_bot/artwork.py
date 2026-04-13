from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UL,
    UP,
    UR,
    WHITE,
    Scene,
    Square,
    Triangle,
    VGroup,
    config,
)

from scenes.alex_up_bot.helpers.mouth import AlexUpBotMouth


class AlexUpBotArtwork(Scene):
    def construct(self):
        config.pixel_width = 500
        config.pixel_height = 500
        config.background_color = None
        head = Square(color="#0EA5E9").set_fill("#0EA5E9", opacity=1)
        eye = Triangle(color=WHITE).set_fill("#30363d", opacity=1).scale(0.25)
        mouth = AlexUpBotMouth()

        left_eye = eye.copy().move_to(head, UL).shift(0.2 * DOWN + 0.2 * RIGHT)
        right_eye = eye.copy().move_to(head, UR).shift(0.2 * DOWN + 0.2 * LEFT)
        mouth.move_to(head, DOWN).shift(0.45 * UP + 0.05 * LEFT)

        eyes = VGroup(left_eye, right_eye).shift(0.1 * DOWN)

        self.add(head, eyes, mouth)
