from manim import Scene

from patch_it_up.helpers.create_code_window import create_code_window


class Verse1(Scene):
    def construct(self):
        lyrics = [
            ("Looking up at my screen, there is a big red cross!", 2.54),
            ("I can't figure it out, I think I'm at a loss!", 2.68),
            ("Oh wait, I've found it out, you won't believe the fix!", 2.54),
            ("Turns out my package wasn't using the latest version!", 2.75),
            ("But now I've found it out, I'm running the pre-commit!", 2.66),
            ("To get it passing took me longer than I'll admit!", 2.71),
            ("I checked it thoroughly, checking all the syntax!", 2.55),
            ("Now time to push my code, hoping that I won't have to...", 2.73),
        ]

        code = create_code_window(
            "\n".join([line for line, _ in lyrics]),
            None,
        )

        self.add(code.background, code.line_numbers)

        line_durations = [duration for _, duration in lyrics]
        assert len(code.code_lines) == len(line_durations)

        for line, duration in zip(code.code_lines, line_durations):
            self.add(line)
            self.wait(duration)
