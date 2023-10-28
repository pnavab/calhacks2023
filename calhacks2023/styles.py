"""Styles for the app."""

import reflex as rx

primary_color = "#1C1C1C"
secondary_color = "#020300"
accent_color_one = "#a4dded"
accent_color_two = "#A3C9A8"
accent_color_three = "#50808E"

border_radius = "0.375rem"
box_shadow = "0px 0px 0px 1px rgba(84, 82, 95, 0.14)"
border = f"1px solid {accent_color_three}"
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
    "background_color": primary_color,
    "::-webkit-scrollbar":  {
        "width": "10px;"  # Width of the scrollbar track */
    },
    "::-webkit-scrollbar-track": {
        "background": primary_color  # /* Background color of the scrollbar track */
    },
    "::-webkit-scrollbar-thumb": {
        "background": secondary_color,  # /* Color of the scrollbar thumb */
        "border-radius": "5px",
    },
    "site-title": {
        "font-size": "30px",
        "color": accent_color_three,
        "text-align": "center",
        "font-weight": "900",
    },
    "question": {
        "max-width": "85%",
        "background-color": accent_color_one,
        "border-radius": "10px 10px 0px 10px",
        "padding": "15px 15px",
        "box_shadow": f"0px 0px 1px 0px {accent_color_one}"
    },
    "answer": {
        "max-width": "85%",
        "background-color": accent_color_two,
        "border-radius": "0px 10px 10px 10px",
        "padding": "15px 15px",
        "box_shadow": f"0px 0px 1px 0px {accent_color_two}"
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
        "background-color": accent_color_three,
        "border-radius": "10px",
        "border": f"1px solid {secondary_color}",
        "box_shadow": f"0px 0px 1px 0px {accent_color_one}"
    },
    "chat-container": {
        "border": f"1px solid {secondary_color}"
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
