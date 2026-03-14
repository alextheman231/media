from manim import Scene, Text, there_and_back


def pulse_title(scene: Scene, title: Text, pulses: int = 3) -> None:
    for _ in range(pulses):
        scene.play(title.animate.scale(1.25), run_time=0.5, rate_func=there_and_back)
