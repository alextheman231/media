from manim import Scene

from patch_it_up.helpers.create_code_window import create_code_window


class Verse1(Scene):
    def construct(self):
        code = create_code_window("""
    Looking up at my screen, there is a big red cross!
    I can't figure it out, I think I'm at a loss!
    Oh wait, I've found it out, you won't believe the fix!
    Turns out my package wasn't using the latest version!
    But now I've found it out, I'm running the pre-commit!
    To get it passing took me longer than I'll admit!
    I checked it thoroughly, checking all the syntax!
    Now time to push my code, hoping that I won't have to...
    """)

        self.add(code)
