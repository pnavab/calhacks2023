"""The home page of the app."""

from calhacks2023 import styles
from calhacks2023.pages import landing
import reflex as rx

def index() -> rx.Component:
    return landing()
