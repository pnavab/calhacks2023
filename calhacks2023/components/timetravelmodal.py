import reflex as rx
from calhacks2023.state import State
from calhacks2023 import styles
from calhacks2023.backend.ai import *
from calhacks2023.styles import *


# def travel_back_in_time(index) -> rx.Component:

#     # Whether the item is active.

#     return rx.link(
#       rx.modal(
#         rx.modal_overlay(
#             rx.modal_content(
#                 rx.modal_header("Are you sure you want to go back in time? This action is irreversible!!"),             
#                 rx.modal_footer(
#                     rx.box(
#                         rx.button(
#                         "Travel", on_click=State.save_checkpoint(),
#                     ), padding = "0.5rem"
#                     ),
#                     rx.button(
#                         "Nevermind!", on_click=State.change_revert_button
#                     )
#                 ),
#             )
#         ),
#         is_open=State.show_revert_button,
#         )
#     )
    