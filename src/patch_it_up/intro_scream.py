from manim import RED, FadeIn, MovingCameraScene, VGroup

from patch_it_up.helpers.create_code_window import create_code_window


class IntroScream(MovingCameraScene):
    def construct(self):
        code = create_code_window(
            code_string="""
Run Setup Job

Current runner version: '2.332.0'
> Runner Image Provisioner
    Hosted Compute Agent
    Version: 20260213.493
    Commit: 5c115507f6dd24b8de37d8bbe0bb4509d0cc0fa3
    Build Date: 2026-02-13T00:28:41Z
    Worker ID: {84988241-b7cd-4fc5-a1a7-d4771c2f0238}
    Azure Region: northcentralus
> Operating System
    Ubuntu
    24.04.3
    LTS
> Runner Image
    Image: ubuntu-24.04
    Version: 20260302.42.1
    Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260302.42/images/ubuntu/Ubuntu2404-Readme.md
    Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260302.42
> GITHUB_TOKEN Permissions
    Contents: read
    Metadata: read
Secret source: Actions
Prepare workflow directory
Prepare all required actions
Getting action download info
Download action repository 'actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd'
Download action repository 'pnpm/action-setup@41ff72655975bd51cab0327fa583b6e92b6d3061'

Error: Can't find 'action.yml', 'action.yaml' or 'Dockerfile'
under '/home/runner/work/media/media/.github/actions/patch-it-up'.
Did you forget to run actions/checkout before running your local action?
""",
        ).scale(0.5)

        self.add(code.background, code.line_numbers)

        error_lines = VGroup(*code.code_lines[-3:])
        output_lines = code.code_lines[:-3]

        for i, line in enumerate(output_lines):
            delay = 0.1 if i < 10 else 0.15
            self.play(FadeIn(line), run_time=delay)

        for line in error_lines:
            line.set_color(RED)

        self.wait(0.5)

        self.add(error_lines)
        self.play(
            self.camera.frame.animate.scale(0.05).move_to(error_lines), duration=3
        )

        self.wait(2)
