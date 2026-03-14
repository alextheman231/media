from manim import (
    BLACK,
    BOLD,
    ORANGE,
    FadeIn,
    RoundedRectangle,
    Scene,
    Succession,
    Text,
    VGroup,
)

from patch_it_up.helpers.create_code_window import create_code_window
from patch_it_up.helpers.pulse import pulse


class ChorusPart1(Scene):
    def construct(self):

        lyrics = [
            ("Now to face the workflow of the damned!", 3.52),
            ("I've gotta push my changes to the branch!", 2.72),
            ("See how the action's gonna act!", 3.03),
        ]

        code = create_code_window(
            "\n".join([line for line, _ in lyrics]),
            None,
        )
        code = create_code_window("\n".join([line for line, _ in lyrics]) + """
        
(media-3.14) ➜  media git:(patch-it-up-now) git push origin patch-it-up-now
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
* [new branch]      patch-it-up-now -> patch-it-up-now
        """).scale(0.68)

        self.add(code.background, code.line_numbers)

        line_durations = [duration for _, duration in lyrics]

        for line, duration in zip(code.code_lines, line_durations):
            self.add(line)
            self.wait(duration)

        title_text = Text(
            "PATCH IT UP NOW!", font="Trattatello", weight=BOLD, color=ORANGE
        )

        background = RoundedRectangle(
            corner_radius=0.2,
            width=title_text.width + 0.6,
            height=title_text.height + 0.4,
        )

        background.set_fill(BLACK, opacity=0.3)
        background.set_stroke(width=0)

        title = VGroup(background, title_text)
        title.set_stroke(ORANGE, width=1)
        title.move_to(title_text)

        self.add_foreground_mobject(title)

        self.play(
            Succession(*[FadeIn(line) for line in code.code_lines[4:]], run_time=1.36),
            pulse(title, pulses=4, duration=1.36, scale_factor=1.5),
        )
