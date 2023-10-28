import reflex as rx
from calhacks2023.state import State
from calhacks2023.backend.ai import *
from .styles import *


class FormState(State):

    # The current question being asked.
    question: str
    default_user_message = "I just spawned in"
    default_model_message = "You are lost in a forest, with no tools or weapons. You notice an old box near you, but are unsure whether you should open it..."

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[dict[str, str]] = [{"user": default_user_message, "model": default_model_message}]
    
    def truncate_chat_history(self):
      if len(self.chat_history) <= 20:
          return self.chat_history
      return self.chat_history[-20:]

    def set_question(self, input):
        self.question = input

    def answer(self):
        # Our chatbot is not very smart right now...
        self.chat_history.append({"user": self.question, "model": "loading"})
        answer = get_ai_response(self.truncate_chat_history(), self.question)
        self.chat_history[-1]["model"] = answer


    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def qa(question, answer) -> rx.Component:
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
          rx.box(
              answer,
              # The answer is on the left.
              text_align="left",
              style=chat_style.get("answer"),
          ),
          style=chat_style.get("answer_row")
      )
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            FormState.chat_history,
            lambda messages: qa(messages["user"], messages["model"]),
        ),
        style=chat_style,
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            on_change=FormState.set_question,
            # style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=FormState.answer,
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
