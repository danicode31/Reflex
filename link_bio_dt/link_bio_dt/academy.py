import reflex as rx
import link_bio_dt.styles.styles as styles
from link_bio_dt.components.text_content import text_title, text_content
from link_bio_dt.components.link_card import link_card, link_card_cert
import link_bio_dt.constants as constants


def academy(title: str) -> rx.Component:
    return rx.box(
        rx.divider(color_scheme="gold"),
        text_title(title),
        rx.flex(
            rx.grid(
                #link_card("2024", " Educación IT - Data Engineer. En curso."),
                link_card(
                    "2018",
                    " UADE - Lic. en Gestión de Tecnología de la Información. En curso.",
                ),
                link_card(
                    "2009", " UADE - Lic. en Administración de Empresas. Incompleto."
                ),
                link_card("2009", " IAMC - Operador de Mercado Bursátil. Finalizado."),
                link_card(
                    "2008",
                    " PICI III - Programa Intensivo de Comercio Internacional - Fundación del Standard Bank. Finalizado.",
                ),
                link_card(
                    "2006",
                    " Escuela Técnica N°14 Libertad - Técnico Electrónico. Finalizado.",
                ),
                spacing="4",
            ),
            align_items="center",
            justify_content="center",
        ),
        rx.spacer(),
        rx.desktop_only(
            rx.vstack(
                rx.text(
                    "Diplomas y Certificados",
                    text_align="center",
                    size="9",
                    border_bottom="1px solid #71624b",
                    padding="30px 0px",
                    text_shadow="2px 2px 5px",
                    margin="20px",
                ),
                rx.flex(
                    rx.grid(
                        link_card_cert(
                            "Certificado de Prompt engineering con Gemini AI y ChatGPT",
                            "/cert/Certificado Taboada.pdf",
                        ),
                        link_card_cert(
                            "Certificado de Python Programming - Educación IT",
                            "/cert/Certificado-Python-Programming-EducaciónIT.pdf",
                        ),link_card_cert(
                            "Certificado de Python Programming - Udemy",
                            "/cert/udemy_python.pdf",
                        ),
                        link_card_cert(
                            "Certificado de Protocolos HTTPS - Educación IT",
                            "/cert/Certificado-Protocolo-HTTPS-EducaciónIT.pdf",
                        ),
                        link_card_cert(
                            "Certificado CCNA CISCO - Carta",
                            "/cert/CCNA1-1Q-letter.pdf",
                        ),
                        link_card_cert(
                            "Certificado CCNA CISCO - Certificado",
                            "/cert/CCNA1-1Q-certificate.pdf",
                        ),
                        
                        link_card_cert(
                            "Certificado Software Tester - Educación IT",
                            "/cert/Certificado-Software-Tester-QA-EducaciónIT.pdf",
                        ),
                        link_card_cert(
                            "Certificado Software Tester QA avanzado - Educación IT",
                            "/cert/Certificado-Software-Tester-QA-Avanzado-EducaciónIT.pdf",
                        ),
                        link_card_cert(
                            "Certificado de Operador de Mercado Bursátil",
                            "/cert/certificado_omb.pdf",
                        ),
                        link_card_cert(
                            "Título de Técnico en Electrónica",
                            "/cert/titulo_tecnico.pdf",
                        ),
                        columns="3",
                        spacing="4",
                        justify="between",
                        width="100%",
                    ),
                    justify_content="center",
                    align_items="center",
                    
                ),
                
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.text(
                    "Diplomas y Certificados",
                    text_align="center",
                    size="8",
                    border_bottom="1px solid #71624b",
                    padding="30px 0px",
                    text_shadow="2px 2px 5px",
                    margin="20px",
                ),
            rx.flex(
                rx.grid(
                    link_card_cert(
                        "Certificado de Prompt engineering con Gemini AI y ChatGPT",
                        "/cert/Certificado Taboada.pdf",
                    ),
                    link_card_cert(
                        "Certificado de Python Programming - Educación IT",
                        "/cert/certificado_python.pdf",
                    ),
                    link_card_cert(
                        "Certificado de Protocolos HTTPS - Educación IT",
                        "/cert/Certificado de Protocolos.pdf",
                    ),
                    link_card_cert(
                        "Certificado CCNA CISCO",
                        "/cert/CCNA1-1Q-letter.pdf",
                    ),
                    link_card_cert(
                        "Certificado Software Tester - Educación IT",
                        "/cert/Certificado Tester 1.pdf",
                    ),
                    link_card_cert(
                        "Certificado Software Tester QA avanzado - Educación IT",
                        "/cert/Certificado Tester 2.pdf",
                    ),
                    link_card_cert(
                        "Certificado de Operador de Mercado Bursátil",
                        "/cert/certificado_omb.pdf",
                    ),
                    link_card_cert(
                        "Título de Técnico en Electrónica",
                        "/cert/titulo_tecnico.pdf",
                    ),
                    columns="2",
                    spacing="4",
                    justify="between",
                    width="auto",
                ),
                justify_content="center",
                align_items="center",
            )
            )
        ),
    )
