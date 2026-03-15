from manim import FadeIn, Scene, VGroup

from patch_it_up.helpers.constants.PATCH_IT_UP_TITLE import PATCH_IT_UP_TITLE
from patch_it_up.helpers.create_code_window import create_code_window
from patch_it_up.helpers.create_text_with_background import create_text_with_background
from patch_it_up.helpers.get_ranges import get_ranges
from patch_it_up.helpers.pulse import pulse
from patch_it_up.post_chorus.helpers.constants.BUILD import BUILD
from patch_it_up.post_chorus.helpers.constants.CHANGE_THE_VERSION import (
    CHANGE_THE_VERSION,
)
from patch_it_up.post_chorus.helpers.constants.CHECKOUT_REPO import CHECKOUT_REPO
from patch_it_up.post_chorus.helpers.constants.FETCH_THE_DOCS import FETCH_THE_DOCS
from patch_it_up.post_chorus.helpers.constants.FORMATTING import FORMATTING
from patch_it_up.post_chorus.helpers.constants.LINTING import LINTING
from patch_it_up.post_chorus.helpers.constants.MERGE_THE_CHANGES import (
    MERGE_THE_CHANGES,
)
from patch_it_up.post_chorus.helpers.constants.SETUP_PACKAGE import SETUP_PACKAGE
from patch_it_up.post_chorus.helpers.constants.START_DEPLOYING import START_DEPLOYING
from patch_it_up.post_chorus.helpers.constants.TESTING import TESTING


class PostChorus(Scene):
    PATCH_IT_UP_TITLE_WITH_BACKGROUND: VGroup = create_text_with_background(
        PATCH_IT_UP_TITLE
    )

    def log_group(
        self,
        group: list[str],
        *,
        duration: float,
        scale: float = 1,
        clear_after: bool = True,
    ):
        code = create_code_window("\n".join(group)).scale(scale)
        self.add(code.background)

        ranges = get_ranges(group)

        for start, end in ranges:
            block = VGroup(*code.code_lines[start:end], *code.line_numbers[start:end])
            self.play(FadeIn(block), run_time=duration / len(group))

        if clear_after:
            self.clear()

    def patch_it_up(self, clear_after: bool = True):
        self.play(
            pulse(
                self.PATCH_IT_UP_TITLE_WITH_BACKGROUND,
                pulses=2,
                duration=1.27,
                scale_factor=4,
            )
        )
        self.play(
            pulse(
                self.PATCH_IT_UP_TITLE_WITH_BACKGROUND,
                pulses=1,
                duration=1.31,
                scale_factor=4,
            )
        )
        if clear_after:
            self.clear()

    def checkout_repo(self):
        self.log_group(CHECKOUT_REPO, duration=1.32, scale=0.3)

    def setup_package(self):
        self.log_group(SETUP_PACKAGE, duration=1.36, scale=0.4, clear_after=False)

    def build(self):
        self.log_group(BUILD, duration=0.28, scale=0.75)

    def formatting(self):
        self.log_group(FORMATTING, duration=0.9, scale=0.5)

    def linting(self):
        self.log_group(LINTING, duration=0.67, scale=0.5)

    def testing(self):
        self.log_group(TESTING, duration=0.65, scale=0.5, clear_after=False)

    def fetch_the_docs(self):
        self.log_group(FETCH_THE_DOCS, duration=1.28, scale=0.75)

    def change_the_version(self):
        self.log_group(CHANGE_THE_VERSION, duration=1.28, clear_after=False)

    def merge_the_changes(self):
        self.log_group(MERGE_THE_CHANGES, duration=1.28, scale=0.5)

    def start_deploying(self):
        self.log_group(START_DEPLOYING, duration=1.28, scale=0.3, clear_after=False)

    def construct(self):
        self.checkout_repo()
        self.setup_package()

        self.patch_it_up()

        self.build()
        self.formatting()
        self.linting()
        self.testing()

        self.patch_it_up()

        self.fetch_the_docs()
        self.change_the_version()

        self.patch_it_up()

        self.merge_the_changes()
        self.start_deploying()

        self.patch_it_up(clear_after=False)
