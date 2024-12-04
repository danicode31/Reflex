import reflex as rx
import link_bio_dt.styles.styles as styles
from link_bio_dt.components.text_content import (
    text_title,
    text_content,
)


def next() -> rx.Component:
    return rx.box(
            rx.divider(color_scheme="gold"),
            text_title("Próximamente"),
            rx.spacer(),
            rx.vstack(
                text_content(
                    "Se están trabajando sobre nuevas secciones y más contenido..."
                ),
                rx.image(
                    src="ml.WebP",
                    alt="ml",
                    margin_y=styles.Spacing.DEFAULT.value,
                ),
                align_items="center",
                flex_direction="column",
            ),
        ),
