"""The dashboard page."""
from calhacks2023.templates import *

import reflex as rx
from calhacks2023.components.textbox import chat


@template(route="/Story", title="StoryPage")
def dashboard() -> rx.Component:
    return rx.vstack(
        rx.heading("StoryTeller", font_size="3em"),
        chat(),
    )
