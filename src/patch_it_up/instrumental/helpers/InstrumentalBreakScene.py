from random import choice, uniform

from manim import MovingCameraScene, RoundedRectangle, Text, VGroup


class InstrumentalBreakScene(MovingCameraScene):
    def scatter_commands(
        self,
        *,
        group_size: int = 1,
        frequency: int = 20,
        duration: float = 10,
        shake_intensity: float = 0.05,
    ):
        all_commands = [
            "git push",
            "pnpm install",
            "pnpm run build",
            "pnpm run lint",
            "eslint",
            "tsc",
            "vitest",
            "prettier --write",
            "husky",
            "zizmor",
            "npm publish",
            "DataError: An error occurred while trying to parse the data.",
            "ENOENT: No such file or directory",
            """
Test Files  1 failed | 57 passed | 1 skipped (59)
     Tests  1 failed | 347 passed (366)
            """,
        ]

        command_colors = ["#58a6ff", "#3fb950", "#f0883e"]
        if not hasattr(self, "background"):
            self.background = (
                RoundedRectangle(width=10, height=5, corner_radius=0.1)
                .set_fill("#161b22", opacity=1)
                .set_stroke("#30363d", width=2)
            )
            self.add(self.background)

        command_groups = [
            [choice(all_commands) for _ in range(group_size)] for _ in range(frequency)
        ]
        for group in command_groups:
            text_group = VGroup(
                *[Text(command, font="Monospace", font_size=16) for command in group]
            )

            for text in text_group:
                text.move_to([uniform(-1, 1), uniform(-1, 1), 0])
                text.rotate(uniform(-0.2, 0.2))
                text.scale(uniform(0.9, 1.2))
                text.set_color(choice(command_colors))

            self.add(text_group)

            original_center = self.camera.frame.get_center()

            self.play(
                *[
                    text.animate.shift([uniform(-4, 4), uniform(-3, 3), 0]).set_opacity(
                        0
                    )
                    for text in text_group
                ],
                self.camera.frame.animate.shift(
                    [
                        uniform(-shake_intensity, shake_intensity),
                        uniform(-shake_intensity, shake_intensity),
                        0,
                    ]
                ),
                run_time=duration / frequency,
            )

            self.camera.frame.move_to(original_center)

            self.remove(text_group)
