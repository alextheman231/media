from manim import (
    BOLD,
    DOWN,
    ORANGE,
    ORIGIN,
    PI,
    RED,
    Rotate,
    Scene,
    Text,
    VGroup,
)

from patch_it_up.helpers.create_code_window import create_code_window
from patch_it_up.helpers.pulse import pulse


class PreChorus1(Scene):
    def construct(self):
        title = Text("PATCH IT UP", font="Trattatello", weight=BOLD, color=ORANGE)

        code = create_code_window("""
Traceback (most recent call last):
  File "/home/runner/work/media/media/src/patch_it_up/verse1.py", line 3, in <module>
    from patch_it_up.helpers.create_code_window import create_code_window
ModuleNotFoundError: No module named 'patch_it_up'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/media/media/.venv/bin/manim", line 8, in <module>
    sys.exit(main())
  File "/home/runner/work/media/media/.venv/lib/python3.14/site-packages/manim/cli/render/commands.py", line 121, in render
    for SceneClass in scene_classes_from_file(file):
  File "/home/runner/work/media/media/.venv/lib/python3.14/site-packages/manim/utils/module_ops.py", line 171, in scene_classes_from_file
    module = get_module(file_path)
  File "/home/runner/work/media/media/.venv/lib/python3.14/site-packages/manim/utils/module_ops.py", line 65, in get_module
    spec.loader.exec_module(module)
ImportError: Failed to import scene module

Error: PATCH IT UUUUUUP!

Run pnpm run lint-tsc

> media@1.0.0 lint-tsc
> tsc --noEmit

src/patch_it_up/helpers/create_code_window.ts:14:5 - error TS2345:
Argument of type 'string | undefined' is not assignable to parameter of type 'string'.

14     code_string,
       ~~~~~~~~~~~

Found 1 error in src/patch_it_up/helpers/create_code_window.ts:14

Error: Process completed with exit code 2.
Error: PATCH IT UUUUUUP!
""").scale(0.4)

        for i in [18, 33, 34]:
            code.code_lines[i].set_color(RED)

        group = VGroup(title, code).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        title.shift(0.15 * DOWN)
        self.add(group)

        self.add(code.background, code.line_numbers, code.code_lines[0:19], title)

        pulse(self, title)

        pulse(
            self,
            VGroup(code.background, code.line_numbers, code.code_lines[0:19]),
            pulses=6,
            duration=3.2,
        )
        self.remove(title)
        self.add(code.code_lines[19:], title)

        pulse(self, title)

        pulse(self, code, pulses=6, duration=2)
        self.play(Rotate(code, 6 * PI, run_time=1.29))

        self.wait(2)
