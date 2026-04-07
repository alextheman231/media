from manim import (
    BOLD,
    ORANGE,
    WHITE,
    FadeIn,
    Scene,
    Succession,
    Text,
)

from patch_it_up.helpers.create_text_with_background import create_text_with_background
from patch_it_up.helpers.pulse import pulse
from utility.create_code_window import create_code_window


class Chorus(Scene):
    def create_chorus(self, lyrics: list[tuple[str, float]], log_text: str) -> None:
        code = create_code_window(
            "\n".join([line for line, _ in lyrics]) + log_text
        ).scale(0.68)

        lyrics_length = len(lyrics)

        lyric_code_lines = code.code_lines[:lyrics_length]
        lyric_line_numbers = code.line_numbers[:lyrics_length]

        code.code_lines[lyrics_length].set_color(code.background.get_color())

        for line in lyric_code_lines:
            line.set_color(WHITE)

        self.add(code.background)

        line_durations = [duration for _, duration in lyrics]

        for line, line_number, duration in zip(
            lyric_code_lines, lyric_line_numbers, line_durations
        ):
            self.add(line, line_number)
            self.wait(duration)

        title = create_text_with_background(
            Text("PATCH IT UP NOW!", font="Trattatello", weight=BOLD, color=ORANGE)
        )
        self.add_foreground_mobject(title)

        self.play(
            Succession(
                *[
                    FadeIn(line, line_number)
                    for line, line_number in zip(
                        code.code_lines[lyrics_length:],
                        code.line_numbers[lyrics_length:],
                    )
                ],
                run_time=1.36,
            ),
            pulse(title, pulses=4, duration=1.36, scale_factor=1.5),
        )

    def construct(self):
        self.create_chorus(
            [
                ("Now to face the workflow of the damned!", 3.52),
                ("I've gotta push my changes to the branch!", 2.72),
                ("See how the action's gonna act!", 3.03),
            ],
            r"""
        
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
        """,
        )

        self.clear()

        self.create_chorus(
            [
                ("I just want my change to be deployed!", 3.52),
                ("The runner's making my blood wanna boil!", 2.72),
                ("But since I misplaced dot-and-slash!", 3.03),
            ],
            r"""
'
(media-3.14) ➜  media git:(patch-it-up-now) git push --force origin patch-it-up-now
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 401 bytes | 401.00 KiB/s, done.
Total 5 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/alextheman231/media.git
 + 7b4c91a...e23a812 patch-it-up-now -> patch-it-up-now (forced update)
        """,
        )
