import reflex as rx
from calhacks2023.state import State
from calhacks2023.backend.ai import *
from calhacks2023.styles import *


def qa(question, answer, image_code) -> rx.Component:
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
        rx.box(
            rx.image(src=f'data:image/png;base64,{image_code}')
        ),
        rx.box(
            rx.box(
                answer,
                # The answer is on the left.
                text_align="left",
                style=base_style.get("answer"),
            ),
            style=stable_styles.get("answer_row")
        ),
        on_click=State.save_checkpoint
    )


def chat() -> rx.Component:
    print(type(State.chat_history))
    return rx.box(
        rx.foreach(
            State.chat_history.reverse(),
            lambda messages: qa(
                messages["user"], messages["model"], messages["image_code"]),
        ),
        style=base_style.get("chat-style"),
    )


def action_bar() -> rx.Component:
    return rx.hstack(

        rx.input(
            placeholder="Ask a question",
            on_change=State.set_question,
            value=State.question,
            on_key_down=State.enter
            # style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            # style=style.button_style,
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
