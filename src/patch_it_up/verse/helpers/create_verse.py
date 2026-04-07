from manim import Scene

from utility.create_code_window import create_code_window


def create_verse(scene: Scene, lyrics: list[tuple[str, int]]) -> None:
    code = create_code_window(
        "\n".join([line for line, _ in lyrics]),
        None,
    )

    scene.add(code.background)

    line_durations = [duration for _, duration in lyrics]
    assert len(code.code_lines) == len(line_durations)

    for line, line_number, duration in zip(
        code.code_lines, code.line_numbers, line_durations
    ):
        scene.add(line, line_number)
        scene.wait(duration)
