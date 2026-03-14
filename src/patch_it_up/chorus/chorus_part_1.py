from manim import (
    Scene,
)

from patch_it_up.chorus.helpers.create_chorus import create_chorus


class ChorusPart1(Scene):
    def construct(self):
        create_chorus(
            self,
            [
                ("Now to face the workflow of the damned!", 3.52),
                ("I've gotta push my changes to the branch!", 2.72),
                ("See how the action's gonna act!", 3.03),
            ],
            r"""
        
(media-3.14) ➜  media git:(patch-it-up-now) git push origin patch-it-up-now
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 401 bytes | 401.00 KiB/s, done.
Total 5 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote: 
remote: Create a pull request for 'patch-it-up-now' on GitHub by visiting:
remote:      https://github.com/alextheman231/media/pull/new/patch-it-up-now
remote: 
To https://github.com/alextheman231/media.git
* [new branch]      patch-it-up-now -> patch-it-up-now
        """,
        )
