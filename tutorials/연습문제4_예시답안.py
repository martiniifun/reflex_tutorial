import reflex as rx


class State(rx.State):
    num = 0

    def plus_one(self):
        self.num += 1

    def minus_one(self):
        self.num -= 1

    def to_zero(self):
        self.num = 0


def index():
    return rx.vstack(
        rx.heading(State.num),
        rx.hstack(
            rx.button("-", on_click=State.minus_one),
            rx.button("0", on_click=State.to_zero),
            rx.button("+", on_click=State.plus_one),
        )
    )


app = rx.App()
app.add_page(index)
app.compile()
