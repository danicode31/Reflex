import reflex as rx
from link_bio_dt.styles import styles


def link_button(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.flex(
                rx.vstack(
                    rx.image(
                        src=image,
                        width=styles.Spacing.LARGE.value,
                        height=styles.Spacing.LARGE.value,
                        alt=alt,
                    ),
                ),
            ),
            color_scheme="gold",
            size=styles.Size.VERY_SMALL.value,
            variant="solid",
            radius="small",
        ),
        href=url,
        is_external=True,
        text_decoration="None",
        opacity="0.6",
        border_radius="1em",
        _hover={
            "opacity": 1,
        },
    )
