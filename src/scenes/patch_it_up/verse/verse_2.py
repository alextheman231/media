from manim import Scene

from scenes.patch_it_up.verse.helpers.create_verse import create_verse


class Verse2(Scene):
    def construct(self):
        create_verse(
            self,
            [
                ("The change has been merged in, workflow scheduled for nine!", 2.54),
                ("I hope by then the workflow will fire up on time!", 2.68),
                ("After a few more hours, I check on it again!", 2.54),
                ("Turns out my timezone wasn't set to my local time now!", 2.75),
                ("Well, nevermind, I'm gonna add a workflow_dispatch!", 2.66),
                ("So I can test it though it feels like an escape hatch!", 2.71),
                ("And once it's done it's gonna update dependencies!", 2.55),
                ("Put up a pull request that's gonna yell at me to...", 2.73),
            ],
        )
