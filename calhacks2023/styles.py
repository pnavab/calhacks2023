"""Styles for the app."""

import reflex as rx

border_radius = "0.375rem"
box_shadow = "0px 0px 0px 1px rgba(84, 82, 95, 0.14)"
border = "1px solid #F4F3F6"
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
    "background_color": "#A4DDED",
    "::-webkit-scrollbar":  {
        "width": "12px;"  # Width of the scrollbar track */
    },
    "::-webkit-scrollbar-track": {
        "background": "#f1f1f1;"  # /* Background color of the scrollbar track */
    },
    "::-webkit-scrollbar-thumb": {
        "background": "#888;"  # /* Color of the scrollbar thumb */
    },
    "site-title": {
        "font-size": "30px",
        "text-align": "center",
        "font-weight": "900",
    },
    "question": {
        "max-width": "85%",
        "background-color": "#999999",
        "border-radius": "10px 10px 0px 10px",
        "padding": "15px 15px",
    },
    "answer": {
        "max-width": "85%",
        "background-color": "#32c4a7",
        "border-radius": "0px 10px 10px 10px",
        "padding": "15px 15px",
    },
    "chat-style": {
        "width": "100%",
        "height": "40rem",
        "overflow-y": "scroll",
        "display": "flex",
        "flex-direction": "column-reverse",
        "align-items": "flex-end"
    },
    "cool_buttons": {
        "background-color": "lightgrey",
    }
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
