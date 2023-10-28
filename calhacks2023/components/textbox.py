import reflex as rx
from calhacks2023.state import State
from calhacks2023.backend.ai import *
from .styles import *


def qa(question, answer, image_code) -> rx.Component:
    return rx.container(
        rx.box(
            rx.box(
                question,
                # The user's question is on the right.
                text_align="right",
                style=chat_style.get("question"),
            ),
            style=chat_style.get("question_row")
        ),
        rx.box(
            rx.image(src=f'data:image/png;base64,{image_code}')
        ),
        rx.box(
            rx.box(
                answer,
                # The answer is on the left.
                text_align="left",
                style=chat_style.get("answer"),
            ),
            style=chat_style.get("answer_row")
        ),
        on_click=State.save_checkpoint
    )


def chat() -> rx.Component:
    print(State.chats[State.cur_chat][1])
    return rx.box(
        rx.foreach(
            State.chat_history.reverse(),
            lambda messages: qa(
                messages["user"], messages["model"], messages["image_code"]),
        ),
        style=chat_style,
    )

def action_bar() -> rx.Component:
    return rx.hstack(

        rx.input(
            placeholder="Ask a question",
            on_change=State.set_question,
            value=State.question,
            # style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            # style=style.button_style,
        ),
        style=action_style,
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
