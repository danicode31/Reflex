import reflex as rx
import link_bio_dt.styles.color as color
import link_bio_dt.styles.styles as styles
    
def navbar() -> rx.Component:
    return rx.center(        
                rx.vstack(
                    rx.heading("Daniel Taboada",font_family="Diphylleia", size="9",color = color.Color.CONTENT.value),
                    margin= styles.Spacer.BIG.value,
                    width= "600px",
                    box_shadow = "-10px -10px #0073b0",
                    border= "2px solid",
                    border_color = "#0073b0",
                    padding= "15px 70px 15px 105px",
                    background_color = "#2f4a6577",
                    text_shadow = "2px 2px 5px",
                     
                    
                )  
    )
            
            