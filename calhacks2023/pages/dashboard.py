"""The dashboard page."""
from calhacks2023.templates import *

import reflex as rx
from calhacks2023.components.textbox import *

@template(route="/", title="Home")
def dashboard() -> rx.Component:
        return rx.vstack(
            rx.heading("StoryTeller", font_size="3em"),
            chat(),
            action_bar(),
        )
