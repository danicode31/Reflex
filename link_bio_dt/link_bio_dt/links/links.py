import reflex as rx
from link_bio_dt.components.link_button import link_button
import link_bio_dt.styles.styles as styles
import link_bio_dt.constants as constants


def links() -> rx.Component:
    return rx.vstack(
        rx.flex(
            link_button("/icons/linkedin.svg", constants.LINKEDIN, "linkedin"),
            link_button("/icons/instagram.svg", constants.INSTAGRAM, "Instagram"),
            link_button("/icons/x.svg", constants.X, "X"),
            # link_button("/icons/discord.svg", constants.DISCORD, "Discord"),
            link_button("/icons/github.svg", constants.GITHUB, "Github"),
            link_button("/icons/email.svg", constants.MAIL, "Correo"),
            flex_direction="row-reverse",
            spacing=styles.Size.LARGE.value,
            margin=styles.Spacing.DEFAULT.value,
            justify_content="center",
        ),
        rx.image(src="/arrow.gif", width="50px"),
        rx.link(
            rx.button(
                "Descargar CV",
                opacity=0.6,
                margin="0px 0px 1em 0px",
                _hover={
                    "opacity": 1,
                },
            ),
            href="/cert/CV Data Engineer - TABOADA.pdf",
            is_external=True,
            justify_content="center",
        ),
        align_items="center",
        width="100%",
        border_top="1px solid white",
        # border_bottom = "1px solid white",
        # border_radius = "100%",
        bg="-webkit-linear-gradient(#272A2D, #161b22)",
    )
