import reflex as rx
import link_bio_dt.styles.styles as st

def footer() -> rx.Component:
    return rx.center(
                rx.flex( 
                rx.text(" DANIEL TABOADA ♥ DATA ENGINEER & CONSULTOR BI © 2024 "
                        ,font_family="Diphylleia", 
                        size="1",
                        color = "#FFFFFF",
                        ),
                margin = '20px',
                padding = '10px'
            )
    )
    