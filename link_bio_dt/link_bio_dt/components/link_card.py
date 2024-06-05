import reflex as rx
from link_bio_dt.styles import styles
from link_bio_dt.components.text_content import text_content


def link_card(anio: str, title: str) -> rx.Component:
    return rx.card(
        
            rx.blockquote(rx.vstack(
                rx.text.strong(anio,font_size=styles.Spacing.BIG.value),
                title,
                color = '#71624b',
                size="3",
                # bg=styles.Color.Color.PRIMARY,
                text_align="center",
                transform="scala(0.5)",
            ),
            color_scheme='gold'  
            ),
            _hover={
                "bg": "#71624b",
                "border": " 3px solid #B08544",
                "text_align": "center",
                "transform": "scale(1.1)",
                "transition": "all 0.3s ease",
            },
        )
  
