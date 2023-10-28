"""The dashboard page."""
from calhacks2023.templates import *

import reflex as rx
from calhacks2023.components.textbox import *
from ..state import State


@template(route="/", title="Home")
def dashboard() -> rx.Component:
    return rx.vstack(
        chat(),
        action_bar(),
        transition="background-image 0.5s",
        background_image=State.gradient_string,
    )
