import reflex as rx
import link_bio_dt.styles.styles as styles

def text_content(text:str) -> rx.Component:
    return rx.text(text,color = styles.color.CONTENT.value, margin = '10px 0px 0px 0px',size='2', text_align = 'justify')





def tecno_utils(text:list) -> rx.Component:
    return rx.popover.root(
                            rx.popover.trigger(
                                rx.button("Tecnologías Utilizadas",color_scheme='gold'),
                            ),
                            rx.popover.content(
                                rx.flex(
                                    rx.vstack(
                                    rx.text(rx.blockquote(' | '.join(text))),
                                    direction='column',
                                    spacing='4',                                   
                                ),
                                align='end'
                            ),
                        ),

                    ),           
                    
                