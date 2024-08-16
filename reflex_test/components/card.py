import reflex as rx
from reflex_test import styles
from reflex_test.components.spline import spline


def card(*children, **props):
    return spline(
        *children,
        box_shadow=styles.box_shadow_style,
        size="3",
        width="100%",
        **props,
    )
