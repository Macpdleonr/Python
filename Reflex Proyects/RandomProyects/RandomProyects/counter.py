import reflex as rx

class StateCounter(rx.State):
    index: int = 0

    def increment(self):
        self.index += 1

    def decrement(self):
        self.index -= 1

@rx.page(route='/counter', title='Counter')
def counter() -> rx.Component:
    return rx.fragment(
        rx.center(
            rx.vstack(
                rx.heading('Counter', size='9'),
                rx.text('First Counter Component'),
                rx.hstack(
                    rx.button('-', on_click=StateCounter.decrement),
                    rx.text(StateCounter.index),
                    rx.button('+', on_click=StateCounter.increment)
                )
            )
        )
    )