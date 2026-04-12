from manim import (
    PI,
    RED,
    Rotate,
    Scene,
    VGroup,
)

from scenes.patch_it_up.helpers.constants.PATCH_IT_UP_TITLE import PATCH_IT_UP_TITLE
from scenes.patch_it_up.helpers.create_text_with_background import (
    create_text_with_background,
)
from scenes.patch_it_up.helpers.pulse import pulse
from utility.create_code_window import create_code_window


class PreChorusBase(Scene):
    def play_pre_chorus(self, durations: tuple[int, int, int, int, int, int]):
        code = create_code_window(r"""
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

        PATCH_IT_UP_TITLE_WITH_BACKGROUND = create_text_with_background(
            PATCH_IT_UP_TITLE
        )

        self.add(
            code.background,
            code.line_numbers[:19],
            code.code_lines[:19],
            PATCH_IT_UP_TITLE_WITH_BACKGROUND,
        )

        self.play(
            pulse(PATCH_IT_UP_TITLE_WITH_BACKGROUND, pulses=2, duration=durations[0])
        )
        self.play(
            pulse(
                PATCH_IT_UP_TITLE_WITH_BACKGROUND,
                pulses=1,
                scale_factor=2.5,
                duration=durations[1],
            ),
        )
        self.play(
            Rotate(
                VGroup(code.background, code.line_numbers[:19], code.code_lines[:19]),
                6 * PI,
                run_time=durations[2],
            )
        )

        self.remove(PATCH_IT_UP_TITLE)
        self.add(
            code.code_lines[19:],
            code.line_numbers[19:],
            PATCH_IT_UP_TITLE_WITH_BACKGROUND,
        )

        self.play(
            pulse(PATCH_IT_UP_TITLE_WITH_BACKGROUND, pulses=2, duration=durations[3])
        )
        self.play(
            pulse(
                PATCH_IT_UP_TITLE_WITH_BACKGROUND,
                pulses=1,
                scale_factor=2.5,
                duration=durations[4],
            ),
        )
        self.play(Rotate(code, 6 * PI, run_time=durations[5]))
