"""Sidebar component for the app."""

from calhacks2023 import styles
from calhacks2023.state import State
import reflex as rx

def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.hstack(
        # The logo.
        rx.image(
            src="/icon.svg",
            height="2em",
        ),
        rx.spacer(),
        # Link to Reflex GitHub repo.
        rx.link(
            rx.center(
                # rx.image(
                box_shadow=styles.box_shadow,
                bg="transparent",
                border_radius=styles.border_radius,
                _hover={
                    "bg": styles.accent_color,
                },
            ),
            href="https://github.com/reflex-dev/reflex",
        ),
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )




def add_sidebar_item() -> rx.Component:

    # Whether the item is active.

    return rx.link(
        rx.button("Start anew", on_click=State.change),
        rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header("Confirm"),
                 rx.input(
            placeholder="Enter your story name:",
            on_change=State.set_name,
            # style=style.input_style,
        ),
                rx.modal_footer(
                    rx.box(
                        rx.button(
                        "Start", on_click=State.create_new,
                    ), padding = "0.5rem"
                    ),
                    rx.button(
                        "Close", on_click=State.change
                    )
                ),
            )
        ),
        is_open=State.show,
        ),
        overflow_y="auto",
        align_items="flex-start",
        padding="0.5em",
    )
# def save_and_close():
#         State.create_new
#         ModalState.change

def sidebar_item(text: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        icon: The icon of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (State.router.page.path == f"/{text.lower()}") | (
        (State.router.page.path == "/") & text == "Home"
    )

    return rx.link(
        rx.hstack(
            rx.text(
                text,
                height="2.5em",
                padding="0.5em",
            ),
            bg=rx.cond(
                active,
                styles.accent_color,
                "transparent",
            ),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            border_radius=styles.border_radius,
            box_shadow=styles.box_shadow,
            width="100%",
            padding_x="1em",
        ),
        on_click=State.switch_tabs(text),
        width="100%",
    )

def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.
    return rx.box(
        rx.vstack(
            sidebar_header(),
            add_sidebar_item(),
            rx.vstack(
                rx.foreach(
                    State.tabs,
                    lambda tab: sidebar_item(
                        tab),
                    ),
                width="100%",
                overflow_y="auto",
                align_items="flex-start",
                padding="1em",
            ),
            rx.spacer(),
            # sidebar_footer(),
            height="100dvh",
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
