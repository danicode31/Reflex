import reflex as rx
import link_bio_dt.styles.styles as styles


def header() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(src="perfil.jpg",
                     width="150px",
                     heigth="150px", 
                     border_radius = "100%",
                    ),
            #rx.chakra.avatar(name="Daniel Taboada", size="sm"),
            rx.blockquote("""Data Engineer (Python, Teradata) | Business Intelligence (Power BI, SSIS, SSAS, SSRS) | Digital Transformation Enthusiast | Information Technology Management Student""", color = styles.color.CONTENT.value
            ,text_align = 'justify'),  
        ),
        
    )
    
            
    
           
