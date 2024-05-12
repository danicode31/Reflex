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
            rx.blockquote("""Data Engineer | Python developer | Teradata | Microsoft Integration Services | SSIS SSAS & SSRS | Power BI | Digital Transformer | Student in Information Technology Management""", color = styles.color.CONTENT.value
            ,text_align = 'justify')    
        ),
    )
    
            
    
           
