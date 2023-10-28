"""The landing page."""

from calhacks2023 import styles
from calhacks2023.templates import template
from calhacks2023.pages import dashboard
import reflex as rx

@template(route="/", title="Home")
def index() -> rx.Component:
    return dashboard()
