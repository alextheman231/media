from patch_it_up.instrumental.helpers.InstrumentalBreakScene import (
    InstrumentalBreakScene,
)


class GuitarSolo(InstrumentalBreakScene):
    def construct(self):
        self.scatter_commands(group_size=5, frequency=50, duration=10.74)
        self.scatter_commands(
            group_size=10, frequency=100, duration=10.63, shake_intensity=0.1
        )
