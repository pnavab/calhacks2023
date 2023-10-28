"""Base state for the app."""

import reflex as rx
from calhacks2023.backend.ai import *
class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """
# The current question being asked.
    question: str
    default_art_style = "cartoon"
    default_user_message = "I just spawned in"
    default_model_message = "You are lost in a forest, with no tools or weapons. You notice an old box near you, but are unsure whether you should open it..."
    default_image_code = get_ai_image(default_model_message, default_art_style)

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[dict[str, str]] = [
        {"user": default_user_message, "model": default_model_message, "image_code": default_image_code}]

    def truncate_chat_history(self):
        if len(self.chat_history) <= 20:
            return self.chat_history
        return self.chat_history[-20:]

    def set_question(self, input):
        self.question = input

    def answer(self):
        self.chat_history.append(
            {"user": self.question, "model": "loading", "image_code": ""})
        ai_answer = get_ai_response(
            self.truncate_chat_history(), self.question)
        print(f"answer is {ai_answer}")
        image_code = get_ai_image(ai_answer, self.default_art_style)
        self.chat_history[-1]["model"] = ai_answer
        self.chat_history[-1]["image_code"] = image_code

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

    def save_checkpoint(self):
        # saves all the context from beginning up until selected point
        new_context = self.chat_history[:3]
