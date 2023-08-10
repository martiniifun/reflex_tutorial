import reflex as rx

from . import style
from .state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=style.answer_style,
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(rx.foreach(
        State.chat_history,
        lambda messages: qa(messages[0], messages[1]),
    ))

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(id="question",
            placeholder="Ask a question",
            on_blur=State.set_question,
            style=style.input_style,
        ),
        rx.button("Ask",
            on_click=State.answer,
            style=style.button_style,
        ))


def index() -> rx.Component:
    return rx.container(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        chat(),
        action_bar(),
    )


app = rx.App()
app.add_page(index)
app.compile()

# """Welcome to Reflex! This file outlines the steps to create a basic app."""
# from rxconfig import config
#
# import reflex as rx
#
# docs_url = "https://reflex.dev/docs/getting-started/introduction"
# filename = f"{config.app_name}/{config.app_name}.py"
#
#
# class State(rx.State):
#     """The app state."""
#
#     pass
#
#
# def index() -> rx.Component:
#     return rx.fragment(
#         rx.color_mode_button(rx.color_mode_icon(), float="right"),
#         rx.vstack(
#             rx.heading("Welcome to Reflex!", font_size="2em"),
#             rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
#             rx.link(
#                 "Check out our docs!",
#                 href=docs_url,
#                 border="0.1em solid",
#                 padding="0.5em",
#                 border_radius="0.5em",
#                 _hover={
#                     "color": rx.color_mode_cond(
#                         light="rgb(107,99,246)",
#                         dark="rgb(179, 175, 255)",
#                     )
#                 },
#             ),
#             spacing="1.5em",
#             font_size="2em",
#             padding_top="10%",
#         ),
#     )