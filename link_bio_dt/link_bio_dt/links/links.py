import reflex as rx
from link_bio_dt.components.link_button import link_button
import link_bio_dt.styles.color as color
import link_bio_dt.styles.styles as styles

def links() -> rx.Component:
    return  rx.flex(          
                link_button("","https://www.linkedin.com/in/daniel-taboada/",color.Color.PRIMARY.value,'linkedin'),
                link_button("","https://www.instagram.com/danieltaboadaok/",color.Color.PRIMARY.value,'Instagram'),
                link_button("","https://twitter.com/taboadad87",color.Color.PRIMARY.value,'Twitter'),
                link_button("","https://github.com/danicode31",color.Color.PRIMARY.value,'github'),
                link_button("","mailto:taboadadanielg@gmail.com",color.Color.PRIMARY.value,'mail')
                ,spacing= '8'
                ,width="100%"
                ,justify='center'
                ,padding = styles.Spacer.DEFAULT.value           
                )
            