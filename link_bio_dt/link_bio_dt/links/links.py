import reflex as rx
from link_bio_dt.components.link_button import link_button
import link_bio_dt.styles.color as color
import link_bio_dt.styles.styles as styles
import link_bio_dt.constants as constants

def links() -> rx.Component:
    return  rx.box(    
                rx.flex(
                                    
                link_button('/icons/linkedin.svg',constants.LINKEDIN,'Linkedin'),
                link_button('/icons/instagram.svg',constants.INSTAGRAM,'Instagram'),
                link_button('/icons/x.svg',constants.X,'Twitter'),
                link_button('/icons/github.svg',constants.GITHUB,'Github'),
                link_button('/icons/email.svg',constants.MAIL,'Correo')
                ,flex_direction = 'row-reverse'
                ,spacing=styles.Size.BIG.value
                ,width="100%"
                ,justify='center'
                ,padding = styles.Spacing.BIG.value 
                )
    )
            
