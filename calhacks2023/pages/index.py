"""The home page of the app."""

from calhacks2023 import styles
from calhacks2023.pages import landing
from calhacks2023.state import State
from calhacks2023.pages import dashboard
import reflex as rx

def index() -> rx.Component:
    return dashboard()
