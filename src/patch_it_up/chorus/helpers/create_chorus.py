from manim import (
    BOLD,
    ORANGE,
    WHITE,
    FadeIn,
    Scene,
    Succession,
    Text,
)

from patch_it_up.helpers.create_code_window import create_code_window
from patch_it_up.helpers.create_text_with_background import create_text_with_background
from patch_it_up.helpers.pulse import pulse


def create_chorus(scene: Scene, lyrics: list[tuple[str, float]], log_text: str) -> None:
    code = create_code_window("\n".join([line for line, _ in lyrics]) + log_text).scale(
        0.68
    )

    lyrics_length = len(lyrics)

    lyric_code_lines = code.code_lines[:lyrics_length]
    lyric_line_numbers = code.line_numbers[:lyrics_length]

    code.code_lines[lyrics_length].set_color(code.background.get_color())

    for line in lyric_code_lines:
        line.set_color(WHITE)

    scene.add(code.background)

    line_durations = [duration for _, duration in lyrics]

    for line, line_number, duration in zip(
        lyric_code_lines, lyric_line_numbers, line_durations
    ):
        scene.add(line, line_number)
        scene.wait(duration)

    title = create_text_with_background(
        Text("PATCH IT UP NOW!", font="Trattatello", weight=BOLD, color=ORANGE)
    )
    scene.add_foreground_mobject(title)

    scene.play(
        Succession(
            *[
                FadeIn(line, line_number)
                for line, line_number in zip(
                    code.code_lines[lyrics_length:], code.line_numbers[lyrics_length:]
                )
            ],
            run_time=1.36,
        ),
        pulse(title, pulses=4, duration=1.36, scale_factor=1.5),
    )
