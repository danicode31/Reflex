import reflex as rx
import link_bio_dt.styles.styles as styles

def link_title(text:str, url:str) -> rx.Component:
    return rx.link(
                rx.button(
                    rx.flex(
                        rx.vstack(
                            rx.text(text,size='5',color = styles.color.CONTENT.value),
                            
                        ),
                    ),
                ),    
                href=url,
                is_external=True,
                text_decoration = "None",
                opacity = "0.6",
                border_radius="1em",
                color_scheme= 'gold',
                _hover={
                        "opacity": 1,
                }
        )
