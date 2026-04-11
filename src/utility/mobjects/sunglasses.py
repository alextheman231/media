from manim import BLACK, LEFT, RIGHT, Circle, Line, ManimColor, Mobject, VGroup
from manim.typing import Point3DLike


class Sunglasses(VGroup):
    def __init__(
        self,
        start: Point3DLike | Mobject = LEFT,
        end: Point3DLike | Mobject = RIGHT,
        *vmobjects,
        lens_size: float = 0.06,
        outline_color: ManimColor | str = BLACK,
        **kwargs,
    ):
        super().__init__(*vmobjects, **kwargs)

        holder = Line(start=start, end=end, color=outline_color)
        lens = Circle(color=outline_color, radius=lens_size).set_fill(
            color=outline_color, opacity=1
        )

        left_lens = lens.copy().move_to(holder.point_from_proportion(1 / 4))
        right_lens = lens.copy().move_to(holder.point_from_proportion(3 / 4))
        lenses = VGroup(left_lens, right_lens)

        self.add(holder, lenses)
