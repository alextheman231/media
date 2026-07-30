from manim import (
    LEFT,
    ORANGE,
    ORIGIN,
    RIGHT,
    RoundedRectangle,
    Scene,
    Text,
    VGroup,
    config,
)


class LexiconArtwork(Scene):
    def construct(self):
        config.pixel_width = 1024
        config.pixel_height = 1024
        config.background_opacity = 0

        page = (
            RoundedRectangle(height=4, width=3, color=ORANGE, stroke_width=5)
            .set_fill("#F8F6F0")
            .set_opacity(1)
        )

        left_page = page.copy().move_to(ORIGIN, aligned_edge=RIGHT)
        right_page = page.copy().next_to(left_page, buff=-0.025)

        lex = (
            Text("Lex", font="Optima", font_size=100, color=ORANGE)
            .move_to(left_page.get_center())
            .shift(0.25 * RIGHT)
        )
        icon = (
            Text("icon", font="Optima", font_size=100, color=ORANGE)
            .move_to(right_page.get_center())
            .shift(0.025 * LEFT)
        )

        logo = VGroup(left_page, right_page, lex, icon)

        self.add(logo)
