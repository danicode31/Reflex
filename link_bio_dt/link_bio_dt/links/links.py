import reflex as rx
from link_bio_dt.components.link_button import link_button
import link_bio_dt.styles.color as color
import link_bio_dt.styles.styles as styles
import link_bio_dt.constants as constants

def links() -> rx.Component:
    return  rx.box(    
                rx.flex(
                                    
                link_button(rx.image(src= 'linkedin.svg'),constants.LINKEDIN,color.Color.PRIMARY.value),
                link_button(rx.image(src= 'instagram.svg'),constants.INSTAGRAM,color.Color.PRIMARY.value),
                link_button(rx.image(src= 'x.svg'),constants.X,color.Color.PRIMARY.value),
                link_button(rx.image(src= 'github.svg'),constants.GITHUB,color.Color.PRIMARY.value),
                link_button(rx.image(src= 'email.svg'),constants.MAIL,color.Color.PRIMARY.value)
                ,spacing= '4'
                ,width="100%"
                ,justify='center'
                ,padding = styles.Spacer.DEFAULT.value           
                )
    )
            