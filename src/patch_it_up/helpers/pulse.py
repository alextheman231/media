from manim import Mobject, Scene, there_and_back


def pulse(
    scene: Scene, m_object: Mobject, *, pulses: int = 3, duration: float = 1.5
) -> None:
    for _ in range(pulses):
        scene.play(
            m_object.animate.scale(1.25),
            run_time=duration / pulses,
            rate_func=there_and_back,
        )
