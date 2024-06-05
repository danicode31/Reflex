import reflex as rx
from link_bio_dt.components.navbar import navbar
from link_bio_dt.components.header import header
from link_bio_dt.components.footer import footer
from link_bio_dt.about_me import about_me
from link_bio_dt.Jobs import jobs
from link_bio_dt.next import next
from link_bio_dt.academy import academy
import link_bio_dt.utils as utils
import link_bio_dt.styles.styles as styles
import link_bio_dt.styles.color as color


def index() -> rx.Component:
    return (
        rx.box(
            utils.lang(),
            navbar(),
            rx.center(
                rx.vstack(
                    header(),
                    about_me("Sobre mi"),
                    jobs("Experiencia Laboral"),
                    academy("Formación Académica"),
                    next(),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin=styles.Spacing.SMALL.value,
                ),
                
            ),
            # links(),
            footer(),
            bg=styles.Color.Color.BACKGROUND.value,
        ),
    )


app = rx.App(
    title=utils.index_title,
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=GTM-KCZF535V"),
        rx.script(
            """window.dataLayer = window.dataLayer || [];
                function gtag(){dataLayer.push(arguments);}
                gtag('js', new Date());

                gtag('config', 'GTM-KCZF535V');
            """
        ),
    ],
)
app.add_page(
    index,
    title=utils.index_title,
    description=utils.index_description,
    image="favicon.ico",
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": utils.index_title},
        {"name": "og:description", "content": utils.index_description},
    ],
)
