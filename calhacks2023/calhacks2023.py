"""Welcome to Reflex!."""

from calhacks2023 import styles

# Import all the pages.
from calhacks2023.pages import *
from calhacks2023.backend.ai import *
import reflex as rx

# Create the app and compile it.
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css?family=Lato",
    ],
    style=styles.base_style
)
app.api.add_api_route(
    path="/",
    endpoint=root
)

app.api.add_api_route(
    path="/get-ai-response",
    endpoint=get_ai_response
)
app.compile()
