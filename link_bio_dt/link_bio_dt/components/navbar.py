import reflex as rx

    
def navbar() -> rx.Component:
    return rx.center(
                rx.vstack(
                    rx.text("Daniel Taboada",height="100%",font_family="Diphylleia", size="9",color = "#FFFFFF"),
                    margin= "2em",
                    width= "auto",
                    box_shadow = "-10px -10px #0073b0",
                    border= "2px solid",
                    border_color = "#0073b0",
                    padding= "10px",
                    background_color = "#2f4a6577",
                    text_shadow = "2px 2px 5px", 
                    
                )  
    )
            
            