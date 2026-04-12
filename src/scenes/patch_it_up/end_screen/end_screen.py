from manim import DrawBorderThenFill, FadeIn, Scene

from scenes.patch_it_up.end_screen.helpers.create_checks_passed_banner import (
    create_checks_passed_banner,
)
from scenes.patch_it_up.end_screen.helpers.text_group import text_group
from scenes.patch_it_up.end_screen.helpers.tick import tick


class EndScreen(Scene):
    def construct(self):
        banner = create_checks_passed_banner(tick, text_group)
        self.play(
            DrawBorderThenFill(banner[0]), DrawBorderThenFill(tick), FadeIn(text_group)
        )

        self.wait(2)
