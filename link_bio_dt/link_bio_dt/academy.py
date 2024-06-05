import reflex as rx
import link_bio_dt.styles.styles as styles
from link_bio_dt.components.text_content import text_title, text_content
from link_bio_dt.components.link_card import link_card
import link_bio_dt.constants as constants


def academy(title: str) -> rx.Component:
    return rx.box(
        rx.divider(color_scheme="gold"),
        text_title(title),
        rx.flex(rx.grid(
            link_card("2018", " UADE - Lic. en Gestión de Tecnología de la Información. En curso."),
            link_card("2009", " UADE - Lic. en Administración de Empresas. Incompleto."),
            link_card("2009", " IAMC - Operador de Mercado Bursátil. Finalizado."),
            link_card("2008", " PICI III - Programa Intensivo de Comercio Internacional - Fundación del Standard Bank. Finalizado."),
            link_card("2006", " Escuela Técnica N°14 Libertad - Técnico Electrónico. Finalizado."),
            spacing="4",
            width = "90%",            
        ),
        align_items = 'center',
        justify_content ='center'
        ),
    )
