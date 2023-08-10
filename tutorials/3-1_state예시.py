import reflex as rx

class State(rx.State):
    num = 0

    def plus_one(self):
        self.num += 1

def index():
    return rx.vstack(
        rx.heading(State.num),
        rx.button("+", on_click=State.plus_one)
    )

app = rx.App()
app.add_page(index)
app.compile()