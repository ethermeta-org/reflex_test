"""The table page."""

from reflex_test.templates import template
from reflex_test.backend.table_state import TableState
from reflex_test.views.table import main_table

import reflex as rx


@template(route="/table", title="Table", on_load=TableState.load_entries)
def table() -> rx.Component:
    """The table page.

    Returns:
        The UI for the table page.
    """
    return rx.vstack(
        rx.heading("Table", size="5"),
        main_table(),
        spacing="8",
        width="100%",
    )
