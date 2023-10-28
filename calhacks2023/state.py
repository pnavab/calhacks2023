"""Base state for the app."""

import reflex as rx
from calhacks2023.backend.ai import *
import random
class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """
# The current question being asked.
    tabs : list[str] = []
    chats : dict[str, list[str, list[dict[str, str]]]] = {}

    scenarios = ["You are stranded on an island...", "You are in a dark forest...","You are in a field...", "You are in a mansion..."]

    question: str
    name: str
    show: bool = False
    landing: bool = True

    cur_chat = "Default Story"
    tabs.append("Default Story")
    default_art_style = "cartoon"
    default_user_message = "I just spawned..."
    default_model_message = "You are lost in a forest, with no tools or weapons. You notice an old box near you, but are unsure whether you should open it..."
    default_image_code = get_ai_image(default_model_message, default_art_style)

    chats[cur_chat] = [default_art_style, [{"user": default_user_message, "model": default_model_message, "image_code": default_image_code}]]
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
        # self.chats[self.cur_chat][1] is the current chat's chat history
        self.chat_history.append(
            {"user": self.question, "model": "loading", "image_code": ""})
        ai_answer = get_ai_response(
            self.truncate_chat_history(), self.question)
        print(f"answer is {ai_answer}")
        image_code = get_ai_image(ai_answer, self.default_art_style)
        self.chat_history[-1]["model"] = ai_answer
        self.chat_history[-1]["image_code"] = image_code
        self.question = ""

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


    def set_name(self, input):
        self.name = input

    def create_new(self):
        self.tabs.append(self.name)
        self.chats[self.name] = ["cartoon", [{"user": "I just spawned...", 'model': random.choice(self.scenarios), "image_code": self.default_image_code}]]
        self.show = not (self.show)
        self.switch_tabs(self.name)

    def change(self):
        self.show = not (self.show)

    def switch_tabs(self, tab):
        self.cur_chat = tab
        self.chat_history = self.chats[tab][1]

    def enter(self,key):
        if key == 'Enter':
            self.answer()

    def save_checkpoint(self, index):
        print(f"double clicked, index is {index}")
        # saves all the context from beginning up until selected point
        cur_chat_history = self.chats[self.cur_chat][1]
        # flip the index since it is passed in flipped from the reverse function
        index = len(cur_chat_history)-index 
        new_context = cur_chat_history[:index]
        new_name = f"Re: {self.cur_chat}"
        cur_art_style = self.chats[self.cur_chat][0]
        self.tabs.append(new_name)
        self.chats[new_name] = [cur_art_style, new_context]
        self.switch_tabs(new_name)