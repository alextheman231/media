from enum import StrEnum
from typing import assert_never

from manim import (
    BLACK,
    DEGREES,
    DOWN,
    LEFT,
    ORIGIN,
    PI,
    RIGHT,
    UP,
    Circle,
    Line,
    ManimColor,
    VGroup,
)

from utility.mobjects.sunglasses import Sunglasses


class Expression(StrEnum):
    HAPPY = "happy"
    NEUTRAL = "neutral"
    SAD = "sad"

    @property
    def mouth_arc(self) -> float:
        match (self):
            case Expression.HAPPY:
                return PI / 6
            case Expression.NEUTRAL:
                return 0
            case Expression.SAD:
                return -PI / 6
            case _:
                assert_never(self)


class StickFigure(VGroup):
    def __init__(
        self,
        *vmobjects,
        outline_color: ManimColor | str = BLACK,
        head_color: ManimColor | str = "#FFB180",
        sunglasses_color: ManimColor | str = BLACK,
        mouth_color: ManimColor | str = BLACK,
        expression: Expression = Expression.HAPPY,
        **kwargs,
    ):
        super().__init__(*vmobjects, **kwargs)
        self._mouth_color = mouth_color
        self.expression = expression

        self.head = Circle(radius=0.3, color=outline_color).set_fill(
            head_color, opacity=1
        )

        self.sunglasses = self._create_sunglasses(sunglasses_color)
        self.mouth = self._create_mouth(expression, mouth_color)

        self.face = VGroup(self.head, self.sunglasses, self.mouth)

        self.body = Line(DOWN * 0.3, DOWN * 1.2, color=outline_color)

        self.left_arm = Line(LEFT * 0.6, ORIGIN, color=outline_color)
        self.right_arm = Line(ORIGIN, RIGHT * 0.6, color=outline_color)

        self.arms = VGroup(self.left_arm, self.right_arm).shift(DOWN * 0.6)

        leg = Line(DOWN * 1.2, DOWN * 2, color=outline_color)

        self.left_leg = leg.copy().rotate(PI / 6, about_edge=UP)
        self.right_leg = leg.copy().rotate(-PI / 6, about_edge=UP)

        self.legs = VGroup(self.left_leg, self.right_leg)

        self.body.next_to(self.head, DOWN, buff=0)
        self.arms.move_to(self.body.point_from_proportion(0.3))
        self.legs.next_to(self.body, DOWN, buff=0)

        self.sunglasses.add_updater(
            lambda sunglasses: sunglasses.become(
                self._create_sunglasses(sunglasses_color)
            )
        )

        self.add(self.face, self.body, self.arms, self.legs)

    def set_expression(self, expression: Expression) -> None:
        self.mouth.become(self._create_mouth(expression, self._mouth_color))
        self.expression = expression

    def set_and_animate_expression(self, expression: Expression):
        self.expression = expression
        return self.mouth.animate.become(
            self._create_mouth(expression, self._mouth_color)
        )

    def _create_sunglasses(self: StickFigure, color: ManimColor | str) -> Sunglasses:
        return Sunglasses(
            start=self.head.point_at_angle((11 * PI) / 12),
            end=self.head.point_at_angle(PI / 12),
            outline_color=color,
        )

    def _create_mouth(self, expression: Expression, color: ManimColor | str) -> Line:
        return Line(
            start=self.head.point_at_angle(-(180 - 25) * DEGREES) + 0.1 * RIGHT,
            end=self.head.point_at_angle(-25 * DEGREES) + 0.1 * LEFT,
            path_arc=expression.mouth_arc,
            color=color,
        )
