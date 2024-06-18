import reflex as rx
import link_bio_dt.styles.color as color
import link_bio_dt.constants as constants
from link_bio_dt.components.text_content import text_footer



def footer() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.link(
                text_footer("DANIEL TABOADA © 2024"),
                href=constants.WEB,
                is_external=False,
                text_decoration="None",
                border_radius="1em",
            ),
            rx.text(
                "DATA SPECIALIST | DATA ENGINEER | CONSULTOR BI",size='1'
            ),
            
            rx.link(
                rx.hstack(
                    text_footer("Built with"),
                    rx.image(src="reflex.jpg", width="15px", heigth="15px",align_items="center"),
                    align_items="center",
                ),
                href=constants.REFLEX_WEB,
                is_external=True,
                text_decoration="None",
                
            ),
            align_items="center",
        ),
        justify_content="center",
        padding="15px",
        bg=color.Color.BGACCORDION.value,
    )

