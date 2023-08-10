import reflex as rx


def index() -> rx.Component:
    return rx.box(
        rx.text("How are you?", text_align="right", margin_y="0.5em"),
        rx.text("I'm fine. Thank you. And you?", text_align="left", margin_y="0.5em"),
        rx.text("I'm fine, too. Thank you.", text_align="right", margin_y="0.5em"),
        rx.text("Bye-bye!", text_align="left", margin_y="0.5em"),
        rx.hstack(
            rx.input(placeholder="질문을 남겨주세요."),
            rx.button("제출"),
        ),
        margin="10%")


app = rx.App()
app.add_page(index)
app.compile()
