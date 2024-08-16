
import reflex as rx
from reflex.components.radix.themes.components.card import Card


class Spline(Card):
    """Spline component."""

    lib_dependencies: list[str] = [
        "@splinetool/runtime@1.5.5",
        "@splinetool/react-spline"
    ]  # Specify extra npm packages to install.


spline = Spline.create