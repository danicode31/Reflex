import reflex as rx
from link_bio_dt.components.navbar import navbar
from link_bio_dt.views.header.header import header
from link_bio_dt.links.links import links
from link_bio_dt.components.footer import footer
import link_bio_dt.styles.styles as styles
from link_bio_dt.contenido import contenido



class State(rx.State):
    pass 



def index() -> rx.Component:
    return rx.box(  
                  navbar(),                  
            rx.center(
                rx.vstack(    
                    header(),
                                            
                    contenido(),
                    max_width = styles.MAX_WIDTH, 
                    width = "100%",
                    margin = styles.Spacer.BIG.value,                       
            )
                ),
                links(),
                
                footer(),
            
            bg = styles.color.BACKGROUND.value,
            
            ),
   
    
        
    

app = rx.App(
    styles = styles.BASE_STYLE,
    
)
app.add_page(index)
app.compile

    
