from manim import RIGHT, RoundedRectangle, SVGMobject, VGroup


def create_checks_passed_banner(tick: SVGMobject, text_group: VGroup) -> VGroup:
    background = RoundedRectangle(corner_radius=0.2)
    banner = VGroup(tick, text_group).arrange(RIGHT)

    background.surround(banner, buff=0.3)
    background.set_fill("#151b23", opacity=1)
    background.set_stroke("#238636")

    group = VGroup(background, banner)

    return group
