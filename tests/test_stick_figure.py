from utility.mobjects.stick_figure import Expression, StickFigure


def test_set_expression_updates_state():
    stick_figure = StickFigure(expression=Expression.HAPPY)
    stick_figure.set_expression(Expression.SAD)
    assert stick_figure.expression == Expression.SAD

def test_set_and_animate_expression_updates_state():
    stick_figure = StickFigure(expression=Expression.HAPPY)

    animation = stick_figure.set_and_animate_expression(Expression.NEUTRAL)

    assert stick_figure.expression == Expression.NEUTRAL
    assert animation is not None

def test_mouth_arc_matches_expression():
    stick_figure = StickFigure(expression=Expression.HAPPY)
    assert stick_figure.expression.mouth_arc == Expression.HAPPY.mouth_arc

    stick_figure.set_expression(Expression.SAD)
    assert stick_figure.expression.mouth_arc == Expression.SAD.mouth_arc
    
    animation = stick_figure.set_and_animate_expression(Expression.NEUTRAL)
    assert stick_figure.expression.mouth_arc == Expression.NEUTRAL.mouth_arc
    assert animation is not None

def test_mouth_arc_values():
    assert Expression.HAPPY.mouth_arc > 0
    assert Expression.SAD.mouth_arc < 0
    assert Expression.NEUTRAL.mouth_arc == 0
