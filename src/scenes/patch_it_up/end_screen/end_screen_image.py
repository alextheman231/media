from manim import Scene

from scenes.patch_it_up.end_screen.helpers.create_checks_passed_banner import (
    create_checks_passed_banner,
)
from scenes.patch_it_up.end_screen.helpers.text_group import text_group
from scenes.patch_it_up.end_screen.helpers.tick import tick


class EndScreen(Scene):
    def construct(self):
        self.add(create_checks_passed_banner(tick, text_group))
