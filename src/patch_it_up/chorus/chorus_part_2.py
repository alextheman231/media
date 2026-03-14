from manim import (
    BLACK,
    BOLD,
    ORANGE,
    WHITE,
    FadeIn,
    RoundedRectangle,
    Scene,
    Succession,
    Text,
    VGroup,
)

from patch_it_up.helpers.create_code_window import create_code_window
from patch_it_up.helpers.pulse import pulse


class ChorusPart2(Scene):
    def construct(self):

        lyrics = [
            ("I just want my change to be deployed!", 3.52),
            ("The runner's making my blood wanna boil!", 2.72),
            ("But since I misplaced dot-and-slash!", 3.03),
        ]

        code = create_code_window("\n".join([line for line, _ in lyrics]) + """
'
(media-3.14) ➜  media git:(patch-it-up-now) git push --force origin patch-it-up-now
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 401 bytes | 401.00 KiB/s, done.
Total 5 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote: 
remote: Create a pull request for 'patch-it-up-now' on GitHub by visiting:
remote:      https://github.com/alextheman231/media/pull/new/patch-it-up-now
remote: 
To https://github.com/alextheman231/media.git
 + 7b4c91a...e23a812 patch-it-up-now -> patch-it-up-now (forced update)
        """).scale(0.68)

        for line in code.code_lines[:3]:
            line.set_color(WHITE)

        code.code_lines[4].set_color(code.background.get_color())

        self.add(code.background, code.line_numbers)

        line_durations = [duration for _, duration in lyrics]

        for line, duration in zip(code.code_lines, line_durations):
            self.add(line)
            self.wait(duration)

        title_text = Text(
            "PATCH IT UP NOW!", font="Trattatello", weight=BOLD, color=ORANGE
        )

        background = RoundedRectangle(corner_radius=0.2)

        background.surround(title_text, buff=0.3)
        background.set_fill(BLACK, opacity=0.3)
        background.set_stroke(width=0)

        title = VGroup(background, title_text)
        title.set_stroke(ORANGE, width=1)

        self.add_foreground_mobject(title)

        self.play(
            Succession(*[FadeIn(line) for line in code.code_lines[4:]], run_time=1.36),
            pulse(title, pulses=4, duration=1.36, scale_factor=1.5),
        )
