import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.container(
        rx.center(
            rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.heading("Examples", font_size="1.5em"),
            rx.link('Counter', href='/counter'),
            rx.link('Rick And Morty', href='/rick_and_morty'),
            )
        )
    )


app = rx.App()
app.add_page(index)
