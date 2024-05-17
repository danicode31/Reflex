import reflex as rx
from link_bio_dt.components.navbar import navbar
from link_bio_dt.views.header.header import header
from link_bio_dt.links.links import links
from link_bio_dt.components.footer import footer
import link_bio_dt.utils as utils
import link_bio_dt.styles.styles as styles
from link_bio_dt.contenido import contenido



class State(rx.State):
    pass 



def index() -> rx.Component:
    return rx.box(
                utils.lang(),  
                navbar(),                  
            rx.center(
                rx.vstack( 
                    header(),          
                    contenido(),
                    max_width = styles.MAX_WIDTH, 
                    width = "100%",
                    margin = styles.Spacing.BIG.value,     
                        
                                         
            )
                ),
            
                links(),
                
                footer(),
            
            bg = styles.Color.Color.BACKGROUND.value,
            
            ),
   
    
        
    

app = rx.App(
    title = utils.index_title,
    styles = styles.BASE_STYLE,
    stylesheets=[

        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
    
    ],
    head_components=[
        rx.script(src='https://www.googletagmanager.com/gtag/js?id=GTM-KCZF535V'),
        rx.script(
            """window.dataLayer = window.dataLayer || [];
                function gtag(){dataLayer.push(arguments);}
                gtag('js', new Date());

                gtag('config', 'GTM-KCZF535V');
            """    
        )
    ]
    
)
app.add_page(
    index,
    title = utils.index_title,
    description= utils.index_description,
    image='favicon.ico',
    meta=[
        {"name": "og:type", "content" :"website"},
        {"name": "og:title", "content": utils.index_title},
        {"name": "og:description", "content": utils.index_description}
    ]
)


    
