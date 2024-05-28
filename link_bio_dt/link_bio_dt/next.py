import reflex as rx
import link_bio_dt.styles.styles as styles
from link_bio_dt.components.link_title import link_title
from link_bio_dt.components.text_content import text_title, text_content_item, text_content


def next() -> rx.Component:
    return rx.flex(
            rx.divider(color_scheme="gold"),
            text_title("Próximamente"),
            rx.spacer(),
                rx.vstack(
                    text_content(
                        "Se están trabajando sobre nuevas secciones y más contenido..."
                    ),
                    rx.image(
                        src="tiempo.jpg",
                        alt="tiempo",
                        margin_y=styles.Spacing.DEFAULT.value,
                    ),
                    rx.button(
                        "Descargar CV",
                        on_click=rx.download(url="/CV Data Engineer - TABOADA.pdf"),
                        opacity=0.6,
                        _hover={
                            "opacity": 1,
                        },
                    ),
                    align="center",
                ),
                flex_direction = 'column'
            ),
    
