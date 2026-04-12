from manim import BLACK, ORANGE, RoundedRectangle, Text, VGroup


def create_text_with_background(text: Text) -> VGroup:
    background = RoundedRectangle(corner_radius=0.2)

    background.surround(text, buff=0.3)
    background.set_fill(BLACK, opacity=0.3)
    background.set_stroke(width=0)

    group = VGroup(background, text)
    group.set_stroke(ORANGE, width=1)

    return group
