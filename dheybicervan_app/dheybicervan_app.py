import reflex as rx

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Cursos en línea", size="9", margin_bottom="1em"),
            rx.text(
                "Mejora tus habilidades con nuestros cursos online en español.",
                margin_bottom="2em",
            ),
            rx.button(
                "Ver cursos",
                color_scheme="teal",
                on_click=rx.redirect("https://dheybicervan.com/cursos"),
            ),
            spacing="1.5em",
            align="center",
        ),
        padding="4em",
    )

app = rx.App()
app.add_page(index, title="dheybicervan - Cursos en línea")
