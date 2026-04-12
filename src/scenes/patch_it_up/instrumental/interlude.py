from scenes.patch_it_up.instrumental.helpers.InstrumentalBreakScene import (
    InstrumentalBreakScene,
)


class Interlude(InstrumentalBreakScene):
    def construct(self):
        self.scatter_commands(group_size=5, frequency=50, duration=10.74)
