from os import getcwd, path

from manim import WHITE, SVGMobject

tick = SVGMobject(
    file_name=path.join(
        getcwd(), "src", "patch_it_up", "end_screen", "helpers", "tick.svg"
    ),
    stroke_color=WHITE,
)
