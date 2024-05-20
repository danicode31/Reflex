import reflex as rx
import link_bio_dt.styles.styles as styles
import link_bio_dt.styles.color as color
import link_bio_dt.constants as constants
from link_bio_dt.components.link_title import link_title
from link_bio_dt.components.text_content import (
    text_content,
    text_title,
    tecno_utils,
    text_content_item,
)


def next() -> rx.Component:
    return rx.box(
        rx.markdown("---"),
        text_title("Próximamente"),
        rx.spacer(),
        rx.flex(
            rx.vstack(
                text_content_item("Se están trabajando sobre nuevas secciones y más contenido..."),
                rx.image(src="tiempo.jpg",alt='tiem',margin_y=styles.Spacing.DEFAULT.value),
            ),
            
        ),
        rx.spacer()
    )