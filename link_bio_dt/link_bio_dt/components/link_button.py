import reflex as rx


def link_button(text:str, url:str, color:str) -> rx.Component:
    return rx.link(
                rx.button(
                    rx.flex(
                        rx.vstack(
                            rx.text(text),
                           
                        ),
                    ),
                ),    
                href=url,
                is_external=True,
                text_decoration = "None",
                opacity = "0.6",
                border_radius="1em",
                _hover={
                        "opacity": 1,
                }
        )
