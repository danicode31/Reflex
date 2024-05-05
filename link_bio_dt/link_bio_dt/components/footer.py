import reflex as rx
import link_bio_dt.styles.styles as st

def footer() -> rx.Component:
    return rx.center(
                rx.flex(   
                rx.image(src="github.svg", heigth="12px", width= "12px"),
                rx.spacer(),
                rx.text(" DANIEL TABOADA ♥ DATA ENGINEER & CONSULTOR BI © 2024 "
                        ,font_family="Diphylleia", 
                        size="1",
                        color = "#FFFFFF",
                        ),
                rx.spacer(),
                rx.image(src="github.svg", heigth="12px", width= "12px"),
                margin = '20px',
                padding = '10px'
            )
    )
    