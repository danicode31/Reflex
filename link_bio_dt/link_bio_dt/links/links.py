import reflex as rx
from link_bio_dt.components.link_button import link_button
import link_bio_dt.styles.color as color
import link_bio_dt.styles.styles as styles

def links() -> rx.Component:
    return  rx.flex(                          
                link_button(rx.image(src= 'linkedin.svg'),"https://www.linkedin.com/in/daniel-taboada/",color.Color.PRIMARY.value),
                link_button(rx.image(src= 'instagram.svg'),"https://www.instagram.com/danieltaboadaok/",color.Color.PRIMARY.value),
                link_button(rx.image(src= 'x.svg'),"https://twitter.com/taboadad87",color.Color.PRIMARY.value),
                link_button(rx.image(src= 'github.svg'),"https://github.com/danicode31",color.Color.PRIMARY.value),
                link_button(rx.image(src= 'email.svg'),"mailto:taboadadanielg@gmail.com",color.Color.PRIMARY.value)
                ,spacing= '4'
                ,width="100%"
                ,justify='center'
                ,padding = styles.Spacer.DEFAULT.value           
                )
            