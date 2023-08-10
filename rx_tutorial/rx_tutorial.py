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
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.container(chat(), action_bar()))


app = rx.App()
app.add_page(index)
app.compile()
