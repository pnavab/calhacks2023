import reflex as rx
from calhacks2023.state import State
from calhacks2023.backend.ai import *
from calhacks2023.styles import *
from calhacks2023 import styles


def travel_back_in_time() -> rx.Component:
    rx.button("Start anew", on_click=State.change,
              style=styles.base_style.get("cool_buttons")),
    # Whether the item is active.
    return rx.link(
        rx.modal(
            rx.modal_overlay(
                rx.modal_content(
                    rx.modal_header(
                        "Are you sure you want to go back in time? This action is irreversible!!"),
                    rx.modal_footer(
                        rx.box(
                            rx.button(
                                "Travel", on_click=State.save_checkpoint(),
                            ), padding="0.5rem"
                        ),
                        rx.button(
                            "Nevermind!", on_click=State.close_revert_modal
                        )
                    ),
                )
            ),
            is_open=State.show_revert_button,
        ),
        overflow_y="auto",
        align_items="flex-start",
        padding="0.5em",
    )


def qa(question, answer, image_code, index) -> rx.Component:
    print(~State.image_loaded)
    print(index is 0)
    return rx.container(
        rx.box(
            rx.box(
                question,
                # The user's question is on the right.
                text_align="right",
                style=base_style.get("question"),
            ),
            style=stable_styles.get("question_row")
        ),
        rx.cond(
            ~ State.image_loaded & index == 0,
            rx.spinner(
                color="lightgrey",
                thickness=2,
                speed="2s",
                size="xl",
            ),
            rx.image(
                src=f'data:image/png;base64,{image_code}', alt='loading image...', border_radius="10px"),
        ),
        rx.box(
            rx.box(
                answer,
                # The answer is on the left.
                text_align="left",
                style=base_style.get("answer"),
            ),
            style=stable_styles.get("answer_row"),
        ),
        travel_back_in_time(),
        on_double_click=State.show_revert_modal(index)
    )


def chat() -> rx.Component:
    # print(type(State.chat_history))
    return rx.box(
        rx.foreach(
            State.chat_history.reverse(),
            lambda messages, index: qa(
                messages["user"], messages["model"], messages["image_code"], index),
        ),
        style=base_style.get("chat-style"),
    )


def action_bar() -> rx.Component:
    return rx.hstack(

        rx.input(
            placeholder="What do you do?",
            on_change=State.set_question,
            value=State.question,
            on_key_down=State.enter,
            background_color=State.accent_color_three,
            # style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=base_style.get("cool_buttons"),
            margin="5px"
        ),
        style=stable_styles.get("action-style"),
    )


# def textbox():
#     return rx.vstack(
#         rx.form(
#             rx.vstack(
#                 rx.input(
#                     placeholder="What do you do?",
#                     id="user_action",
#                     style=input_style,
#                 ),
#                 rx.button("Submit", type_="submit"),
#                 style=box_style,
#             ),
#             on_submit=FormState.handle_submit,
#         ),
#         rx.divider(),
#         rx.heading("Results"),
#         rx.text(FormState.form_data.to_string()),
#     )
