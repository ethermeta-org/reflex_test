"""Welcome to Reflex!."""

# Import all the pages.
from reflex_test.pages import *
from reflex_test import styles

import reflex as rx


# Create the app.
app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
    title="Dashboard Template",
    description="A dashboard template for Reflex.",
)
