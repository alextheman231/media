from manim import DOWN, ORIGIN, Scene, VGroup

from scenes.patch_it_up.helpers.constants.PATCH_IT_UP_TITLE import PATCH_IT_UP_TITLE
from utility.create_code_window import create_code_window


class PatchItUpArtwork(Scene):
    def construct(self):
        code = create_code_window(
            code_string=r"""
Run pnpm run build
> @alextheman/github-actions@6.3.0 build
> tsdown

ℹ entry: src/index.ts
ℹ target: node22.0.0
ℹ tsconfig: tsconfig.json
ℹ Build start
ℹ Cleaning 6 files
ℹ [CJS] dist/index.cjs      21.32 kB │ gzip:  7.07 kB
ℹ [CJS] dist/index.cjs.map  84.02 kB │ gzip: 18.84 kB
ℹ [CJS] 2 files, total: 105.33 kB
ℹ [CJS] dist/index.d.cts  21.82 kB │ gzip: 4.53 kB
ℹ [CJS] 1 files, total: 21.82 kB
✔ Build complete in 1781ms
ℹ [ESM] dist/index.js      17.93 kB │ gzip:  6.46 kB
ℹ [ESM] dist/index.js.map  80.25 kB │ gzip: 18.25 kB
ℹ [ESM] dist/index.d.ts    21.82 kB │ gzip:  4.53 kB
ℹ [ESM] 3 files, total: 120.00 kB
✔ Build complete in 1785ms

Run pnpm run lint
✖ Error: Cannot find action './.github/actions/lint-ci.yml'

Error: Process completed with exit code 1.
""",
        ).scale(0.68)

        group = VGroup(PATCH_IT_UP_TITLE, code).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        PATCH_IT_UP_TITLE.shift(0.15 * DOWN)
        self.add(group)
