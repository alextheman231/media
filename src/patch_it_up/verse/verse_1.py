from manim import Scene

from patch_it_up.verse.helpers.create_verse import create_verse


class Verse1(Scene):
    def construct(self):
        create_verse(
            self,
            [
                ("Looking up at my screen, there is a big red cross!", 2.54),
                ("I can't figure it out, I think I'm at a loss!", 2.68),
                ("Oh wait, I've found it out, you won't believe the fix!", 2.54),
                ("Turns out my package wasn't using the latest version!", 2.75),
                ("But now I've found it out, I'm running the pre-commit!", 2.66),
                ("To get it passing took me longer than I'll admit!", 2.71),
                ("I checked it thoroughly, checking all the syntax!", 2.55),
                ("Now time to push my code, hoping that I won't have to...", 2.73),
            ],
        )
