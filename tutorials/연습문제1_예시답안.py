import pandas as pd
import reflex as rx

nba_data = pd.read_csv(
    "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"
)

data = rx.data(
    "bar",
    x=["Cats", "Dogs", "Birds", "Fish", "Reptiles"],
    y=[1, 2, 3, 4, 10],
)


def index():
    rx.vstack(
        rx.text("Hello World!", as_="i"),
        rx.text("Hello World!", as_="s"),
        rx.heading("Hello World!", size="4xl", color="green"),
        rx.markdown("### Hello World!"),
        rx.hstack(
            rx.badge("Example", variant="solid", color_scheme="green"),
            rx.badge("Example", variant="subtle", color_scheme="green"),
            rx.badge("Example", variant="outline", color_scheme="green"),
        ),
        rx.data_table(
            data=nba_data[["Name", "Height", "Age"]],
            pagination=True,
            search=True,
            sort=True,
        ),
        rx.chart(
            rx.bar(
                data=rx.data(
                    "bar",
                    x=["Cats", "Dogs", "Birds", "Fish", "Reptiles"],
                    y=[1, 2, 3, 4, 10],
                ),
                style={
                    "data": {
                        "fill": "rgb(107,99,246)",
                        "stroke": "black",
                        "strokeWidth": 2,
                    }
                },
            ),
            domain_padding={"x": 20, "y": 0},
        )
    )
