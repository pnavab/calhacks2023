"""Styles for the app."""

import reflex as rx
from .state import State

primary_color = "#1C1C1C"
secondary_color = "#939791"

border_radius = "0.375rem"
box_shadow = "0px 0px 0px 1px rgba(84, 82, 95, 0.14)"
border = f"1px solid {State.accent_color_three}"
text_color = "black"
accent_text_color = "#1A1060"
accent_color = "#F5EFFE"
hover_accent_color = {"_hover": {"color": accent_color}}
hover_accent_bg = {"_hover": {"bg": accent_color}}
content_width_vw = "90vw"
sidebar_width = "20em"
background_color = "#434654"

template_page_style = {"padding_top": "2em", "padding_x": ["auto", "2em"]}

template_content_style = {
    "width": "100%",
    "align_items": "flex-start",
    "box_shadow": box_shadow,
    "border_radius": border_radius,
    "padding": "1em",
    "margin_bottom": "2em",
}

link_style = {
    "color": text_color,
    "text_decoration": "none",
    **hover_accent_color,
}

overlapping_button_style = {
    "background_color": "white",
    "border": border,
    "border_radius": border_radius,
}

stable_styles = {
    "question_row": {
        "display": "flex",
        "flex-direction": "row",
        "justify-content": "right",
        "margin": "10px 0px",
    },
    "answer_row": {
        "display": "flex",
        "flex-direction": "row",
        "justify-content": "left",
        "margin": "10px 0px",
    },
    "action-style": {
        "width": "800px;",
    }
}


base_style = {
    "background-color": secondary_color,
    "::-webkit-scrollbar":  {
        "width": "10px;"  # Width of the scrollbar track */
    },
    "::-webkit-scrollbar-track": {
        # /* Background color of the scrollbar track */
        "background": State.accent_color_one
    },
    "::-webkit-scrollbar-thumb": {
        "background": State.accent_color_two,  # /* Color of the scrollbar thumb */
        "border-radius": "5px",
    },
    "site-title": {
        "font-size": "30px",
        "color": State.accent_color_three,
        "text-align": "center",
        "font-weight": "900",
    },
    "question": {
        "max-width": "85%",
        "background-color": State.accent_color_one,
        "border-radius": "10px 10px 0px 10px",
        "padding": "15px 15px",
        "box_shadow": f"0px 0px 1px 0px {State.accent_color_one}",
        "color": "black",
        "mix-blend-mode": "difference"
    },
    "answer": {
        "max-width": "85%",
        "background-color": State.accent_color_two,
        "border-radius": "0px 10px 10px 10px",
        "padding": "15px 15px",
        "box_shadow": f"0px 0px 1px 0px {State.accent_color_two}",
        "color": "black",
        "mix-blend-mode": "difference"
    },
    "chat-style": {
        "width": "100%",
        "max-height": "45rem",
        "overflow-y": "scroll",
        "display": "flex",
        "flex-direction": "column-reverse",
        "align-items": "flex-end"
    },
    "cool_buttons": {
        "background-color": State.accent_color_three,
        "border-radius": "10px",
        "border": f"1px solid {secondary_color}",
        "box_shadow": f"100px 100px 1px 0px {State.accent_color_one}",
        "padding": "10px 12px",
    },
    "chat-container": {
        "border": f"1px solid {secondary_color}",
        "padding": "20px",
        "margin": "0px 0px 20px 20px"
    },
    "ask_button": {
        "background-color": State.accent_color_three,
        "border-radius": "10px",
        "border": f"1px solid {secondary_color}",
        "box_shadow": f"0px 0px 1px 0px {State.accent_color_one}",
        "padding": "10px",
        "margin-left": "10em",
        "margin-top": "2em",
    },
}

markdown_style = {
    "code": lambda text: rx.code(text, color="#1F1944", bg="#EAE4FD"),
    "a": lambda text, **props: rx.link(
        text,
        **props,
        font_weight="bold",
        color="#03030B",
        text_decoration="underline",
        text_decoration_color="#AD9BF8",
        _hover={
            "color": "#AD9BF8",
            "text_decoration": "underline",
            "text_decoration_color": "#03030B",
        },
    ),
}
