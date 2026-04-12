from manim import BOLD, DOWN, GRAY, Text, VGroup

text_group = VGroup(
    Text("All workflows have passed", font="Helvetica", weight=BOLD),
    Text("1 successful check", font="Helvetica", color=GRAY),
).arrange(DOWN)
