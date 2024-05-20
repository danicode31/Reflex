import reflex as rx
import link_bio_dt.styles.color as color
import link_bio_dt.constants as constants
from link_bio_dt.components.text_content import text_footer
from link_bio_dt.links.links import links


def footer() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.link(
                text_footer("DANIEL TABOADA © 2024"),
                href=constants.WEB,
                is_external=False,
                text_decoration="None",
                opacity="0.6",
                border_radius="1em",
                color_scheme="gold",
                _hover={
                    "opacity": 1,
                },
            ),
            text_footer("DATA SPECIALIST | DATA ENGINEER | CONSULTOR BI"),
            links(),
            rx.link(
                rx.hstack(
                    rx.text(
                        "Built with",
                        size="1",
                        color=color.Color.CONTENT.value,
                        opacity="80%",
                    ),
                    rx.image(src="reflex.jpg", width="15px", heigth="15px"),
                ),
                href=constants.REFLEX_WEB,
                is_external=True,
                text_decoration="None",
                opacity="0.6",
                border_radius="1em",
                _hover={
                    "opacity": 1,
                },
            ),
            align_items="center",
        ),
        justify_content="center",
        padding="15px",
        bg=color.Color.BGACCORDION.value,
    )
