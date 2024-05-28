import reflex as rx
import link_bio_dt.styles.styles as styles


def text_content(text: str) -> rx.Component:
    return rx.text(
        text,
        font_family=styles.Font.DEFAULT.value,
        color=styles.Color.Color.CONTENT.value,
        margin="10px 0px 0px 0px",
        size="3",
        text_align="justify",
    )


def text_content_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon("square-check-big"),
        rx.text(
            rx.text(
                text,
                font_family=styles.Font.DEFAULT.value,
                color=styles.Color.Color.CONTENT.value,
                margin="5px",
                text_align="justify",
            ),
            size='3',
        ),
        opacity="0.6",
        _hover={
            "opacity": 1,
        },
    )


def tecno_utils(text: str) -> rx.Component:
    return (
        rx.popover.root(
            rx.popover.trigger(
                rx.button("Tecnologías Utilizadas", color_scheme="gold"),
                opacity="0.6",
                _hover={
                    "opacity": 1,
        },
            ),
            rx.popover.content(
                rx.flex(
                    rx.vstack(
                        rx.text(rx.blockquote(" | ".join(text), color_scheme="gold")),
                        rx.popover.close(
                            rx.button("Cerrar", color_scheme="gold"),
                        ),
                    ),
                    direction="column",
                    spacing="4",
                ),
                align="end",
                min_width="auto",
            ),
            modal=True,
        ),
    )


def text_title(text: str) -> rx.Component:
    return rx.heading(
        text,
        font_family=styles.Font.TITLE.value,
        size="9",
        color=styles.Color.Color.PRIMARY.value,
        padding="30px 0px",
        text_shadow="2px 2px 5px",
    )


def text_footer(text: str) -> rx.Component:
    return rx.text(
        text,
        font_family=styles.Font.DEFAULT.value,
        size='2',
        color=styles.Color.Color.CONTENT.value,
        opacity="0.6",
        _hover={
            "opacity": "1"},
    )
