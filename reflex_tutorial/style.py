import reflex as rx

shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    color=rx.color_mode_cond(
        light="rgb(107,99,246)",
        dark="rgb(179, 175, 255)",
    ))

question_style = message_style | dict(
    bg="#F5EFFE", margin_left=chat_margin)
answer_style = message_style | dict(
    bg="#DEEAFD", margin_right=chat_margin)

input_style = dict(border_width="1px", padding="1em", box_shadow=shadow)
button_style = dict(bg="#CEFFEE", box_shadow=shadow, color="rgb(107,99,246)")
