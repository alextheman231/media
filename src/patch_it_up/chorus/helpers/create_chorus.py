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


def create_chorus(
    scene: Scene, lyrics: list[tuple[str, float]], code_text: str
) -> None:
    code = create_code_window(
        "\n".join([line for line, _ in lyrics]) + code_text
    ).scale(0.68)

    lyric_code_lines = code.code_lines[:3]
    lyric_line_numbers = code.line_numbers[:3]

    code.code_lines[3].set_color(code.background.get_color())

    for line in lyric_code_lines:
        line.set_color(WHITE)

    scene.add(code.background)

    line_durations = [duration for _, duration in lyrics]

    for line, line_number, duration in zip(
        lyric_code_lines, lyric_line_numbers, line_durations
    ):
        scene.add(line, line_number)
        scene.wait(duration)

    title_text = Text("PATCH IT UP NOW!", font="Trattatello", weight=BOLD, color=ORANGE)

    background = RoundedRectangle(corner_radius=0.2)

    background.surround(title_text, buff=0.3)
    background.set_fill(BLACK, opacity=0.3)
    background.set_stroke(width=0)

    title = VGroup(background, title_text)
    title.set_stroke(ORANGE, width=1)

    scene.add_foreground_mobject(title)

    scene.play(
        Succession(
            *[
                FadeIn(line, line_number)
                for line, line_number in zip(code.code_lines[3:], code.line_numbers[3:])
            ],
            run_time=1.36,
        ),
        pulse(title, pulses=4, duration=1.36, scale_factor=1.5),
    )
