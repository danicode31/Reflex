import reflex as rx
import link_bio_dt.styles.color as color
import link_bio_dt.constants as constants

def footer() -> rx.Component:
    return rx.flex(
                rx.vstack(
                        rx.text(" DANIEL TABOADA - DATA ENGINEER & CONSULTOR BI © 2024 ", 
                        font_family="Diphylleia", 
                        size="1",
                        color = "#FFFFFF",
                        opacity = "50%"),
                        
                        rx.link(rx.text("Built with Reflex",
                        size="1",
                        text_align_content = 'center',
                        color = color.Color.PRIMARY.value,
                        opacity = "80%",

                        
                        ), href=constants.REFLEX_WEB,
                        is_external=True,
                        text_decoration = "None",
                        opacity = "0.6",
                        border_radius="1em",
                        _hover={
                                "opacity": 1,
                        },
                        
                        ),                                
       
                ),
        justify_content = 'center',
        align_items = 'center',
        padding = "5px",
        bg = color.Color.SECONDARY.value 
        )