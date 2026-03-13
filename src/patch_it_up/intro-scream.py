from manim import RED, Code, FadeIn, Scene, VGroup


class PatchItUp(Scene):
    def construct(self):
        code = Code(
            code_string="""
Run Setup Job

Current runner version: '2.332.0'
> Runner Image Provisioner
    Hosted Compute Agent
    Version: 20260213.493
    Commit: 5c115507f6dd24b8de37d8bbe0bb4509d0cc0fa3
    Build Date: 2026-02-13T00:28:41Z
    Worker ID: {aed1c625-6eff-4b98-8bd4-b94e5359c79e}
    Azure Region: northcentralus
> Operating System
    Microsoft Windows Server 2025
    10.0.26100
    Datacenter
> Runner Image
    Image: windows-2025
    Version: 20260302.43.1
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
            language="bash",
            background="rectangle",
            paragraph_config={"font": "Monospace"},
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

        self.play(
            error_lines.animate.scale(100).move_to(self.camera.frame_center), run_time=2
        )
