from manim import Mobject, ScaleInPlace, Succession, there_and_back


def pulse(m_object: Mobject, *, pulses: int = 3, duration: float = 1.5):
    return Succession(
        *[
            ScaleInPlace(
                m_object,
                scale_factor=1.25,
                rate_func=there_and_back,
                run_time=duration / pulses,
            )
            for _ in range(pulses)
        ]
    )
