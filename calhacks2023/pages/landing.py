"""The landing page."""

from calhacks2023.templates import template
import reflex as rx


def landing() -> rx.Component:
    return rx.vstack(
            rx.heading("Press create story to create stories!", font_size="3em"),
    )
