"""Base state for the app."""

import reflex as rx
from calhacks2023.backend.ai import *
import random
import asyncio


class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """
# The current question being asked.
    tabs: list[str] = []
    chats: dict[str, list[str, list[dict[str, str]]]] = {}

    scenarios = ["You are stranded on an island and don't remember how you got there. To your left is a coconut and a half sharpened rock that looks like someone else tried shaping into a knife. You hear a faint but aggressive pack of monkeys howling in the distance...", "You are lost in a forest, with no tools or weapons. You notice an old box near you, but are unsure whether you should open it...",
                 "You wake up in a maze with walls 3 times your height. Suddenly, you notice a looming figure emerge from the shadows behind you. It seems to be holding a large club...", "You are in a mansion, yet it seems eerily quiet. It seems abandoned, and you seem to be the only one home yet don't remember how you got there..."]

    question: str
    name: str
    show: bool = False
    show_revert_button = False
    index_to_revert: int = 0
    temp_question: str

    accent_color_one = "#a4dded"
    accent_color_two = "#A3C9A8"
    accent_color_three = "lightgrey"

    gradient_string = f"linear-gradient(180.0deg, {accent_color_one} 0.75%, {accent_color_two} 88.52%)"
    print(gradient_string)

    @rx.background
    async def change_background_color(self, prompt):
        colors = get_hex_codes(prompt)
        async with self:
            self.accent_color_one = "#"+colors[0]
            self.accent_color_two = "#"+colors[1]
            self.gradient_string = f"linear-gradient(180.0deg, {self.accent_color_one} 5%, {self.accent_color_two} 88.52%)"

    @rx.background
    async def set_background_image(self, prompt, art_style):
        code = get_ai_image(prompt, art_style)
        async with self:
            self.chat_history[-1]["image_code"] = code
            self.image_loaded = True

    forest: str = "#A9A9A9"
    ocean: str = "#A9A9A9"
    medieval: str = "#A9A9A9"
    steampunk: str = "#A9A9A9"
    cartoon: str = "#A9A9A9"

    cur_chat = "Default Story"
    tabs.append(cur_chat)
    default_art_style = "cartoon"
    default_user_message = "I just spawned..."
    default_model_message = "You are lost in a forest, with no tools or weapons. You notice an old box near you, but are unsure whether you should open it..."
    default_image_code = get_ai_image(default_model_message, default_art_style)

    chats[cur_chat] = [default_art_style, [
        {"user": default_user_message, "model": default_model_message, "image_code": default_image_code}]]
    chat_history: list[dict[str, str]] = chats[cur_chat][1]

    def truncate_chat_history(self):
        if len(self.chat_history) <= 20:
            return self.chat_history
        return self.chat_history[-20:]

    def set_question(self, input):
        self.question = input

    image_loaded: bool = True

    def toggle_loaded(self):
        self.image_loaded = not (self.image_loaded)

    @rx.background
    async def answer(self):
        # self.chats[self.cur_chat][1] is the current chat's chat history
        async with self:
            self.image_loaded = False
            self.chat_history.append(
                {"user": self.temp_question, "model": "loading", "image_code": ""})
            ai_answer = get_ai_response(
                self.truncate_chat_history(), self.temp_question)
            yield State.stream(ai_answer)
            yield State.change_background_color(ai_answer)
            yield State.set_background_image(ai_answer, self.chats[self.cur_chat][0])

    def handle_answer(self):
        self.temp_question = self.question
        self.question = ""
        yield State.answer()

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

    def set_name(self, input):
        self.name = input

    def create_new(self):
        theme = ""
        if (self.forest == "black"):
            theme = "forest"
        elif (self.steampunk == "black"):
            theme = "steampunk"
        elif (self.ocean == "black"):
            theme = "ocean"
        elif (self.cartoon == "black"):
            theme = "cartoon"
        elif (self.medieval == "black"):
            theme = "medieval"
        if not self.name in self.tabs:
            self.tabs.append(self.name)

            random_scenario = random.choice(self.scenarios)
            image_code = get_ai_image(random_scenario, theme)
            self.chats[self.name] = [theme, [
                {"user": "I just spawned...", 'model': random_scenario, "image_code": image_code}]]

            # self.chats[self.name] = [theme, [{"user": "I just spawned...", 'model': random.choice(
            #     self.scenarios), "image_code": self.default_image_code}]]

            self.show = not (self.show)
            self.switch_tabs(self.name)
        else:
            print("name already exists")

    def change(self):
        self.show = not (self.show)

    def show_revert_modal(self, index):
        self.show_revert_button = True
        if index is not None:
            self.index_to_revert = index
        print(self.show_revert_button)

    def close_revert_modal(self):
        self.show_revert_button = False

    def switch_tabs(self, tab):
        self.cur_chat = tab
        self.chat_history = self.chats[tab][1]

    async def enter(self, key):
        if key == 'Enter':
            self.temp_question = self.question
            self.question = ""
            yield State.answer()

    def save_checkpoint(self):
        # print(f"double clicked, index is {self.index}")
        # saves all the context from beginning up until selected point
        cur_chat_history = self.chat_history
        # flip the index since it is passed in flipped from the reverse function
        self.index_to_revert = len(cur_chat_history)-self.index_to_revert
        old_name = self.cur_chat
        new_context = cur_chat_history[:self.index_to_revert]
        tab_index = self.tabs.index(old_name)
        self.tabs.pop(tab_index)
        self.name = f"Re: {self.cur_chat}"
        self.tabs.append(self.name)
        self.chats[self.name] = [self.chats[old_name][0], new_context]
        self.switch_tabs(self.name)
        self.show_revert_button = False
        # cur_art_style = self.chats[self.cur_chat][0]
        # self.chats[new_name] = [cur_art_style, new_context]

    def toggle_forest(self):
        self.steampunk = "#A9A9A9"
        self.medieval = "#A9A9A9"
        self.ocean = "#A9A9A9"
        self.forest = "black"
        self.cartoon = "#A9A9A9"

    def toggle_steampunk(self):
        self.steampunk = "black"
        self.medieval = "#A9A9A9"
        self.ocean = "#A9A9A9"
        self.forest = "#A9A9A9"
        self.cartoon = "#A9A9A9"

    def toggle_ocean(self):
        self.steampunk = "#A9A9A9"
        self.medieval = "#A9A9A9"
        self.ocean = "black"
        self.forest = "#A9A9A9"
        self.cartoon = "#A9A9A9"

    def toggle_medieval(self):
        self.steampunk = "#A9A9A9"
        self.medieval = "black"
        self.ocean = "#A9A9A9"
        self.forest = "#A9A9A9"
        self.cartoon = "#A9A9A9"

    def toggle_cartoon(self):
        self.steampunk = "#A9A9A9"
        self.medieval = "#A9A9A9"
        self.ocean = "#A9A9A9"
        self.forest = "#A9A9A9"
        self.cartoon = "black"

    @rx.background
    async def stream(self, ai_answer):
        async with self:
            self.chat_history[-1]["model"] = ""

            for i in range(len(ai_answer)):
                # Pause to show the streaming effect.
                random_number = random.uniform(0.05, 0.08)
                await asyncio.sleep(random_number)
                # Add one letter at a time to the output.
                # self.chat_history[-1]["model"][i] = answer[i]
                self.chat_history[-1]["model"] = ai_answer[0: i]
                yield

            # self.chats[self.cur_chat][1][-1]["model"] = self.chat_history[0]["model"]
            # yield
