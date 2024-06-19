import reflex as rx
import link_bio_dt.styles.color as color
import link_bio_dt.styles.styles as styles


def navbar() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.image(
                src="/R.WebP",
                width=styles.MAX_WIDTH,
                alt="presentacion",
            ),
        ),
        align_items="center",
        justify_content="center",
    )
