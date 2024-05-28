import reflex as rx
import link_bio_dt.styles.color as color


def link_title(text: str, image: str, url: str) -> rx.Component:
    return rx.hstack(
        rx.image(src=image, width="64px", heigth="64px", border_radius="20%"),
        rx.link(
            rx.button(
                rx.flex(
                    rx.icon("arrow-right"),
                    rx.text(text, size="6", color=color.Color.CONTENT.value),
                ),
            ),
            href=url,
            is_external=True,
            text_decoration="None",
            border_radius="1em",
            color_scheme="gold",
            
        ),
        opacity="0.6",
        _hover={
            "opacity": "1",
        },
        align_items="center",
    )
