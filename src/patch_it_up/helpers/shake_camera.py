from random import uniform

from manim import Camera


def shake_camera(camera: Camera, shake_intensity: float = 0.05):
    return (
        camera.frame.animate.shift(
            [
                uniform(-shake_intensity, shake_intensity),
                uniform(-shake_intensity, shake_intensity),
                0,
            ]
        ),
    )
