import reflex as rx
import link_bio_dt.styles.styles as styles
import link_bio_dt.styles.color as color

def contenido() -> rx.Component:
    return  rx.box(
                rx.heading("""Sobre mi""",
                        size= '5',
                        color = color.Color.PRIMARY.value,
                        high_contrast=True,
                        padding = "30px 0px"
                        ),
                rx.box(
                    rx.text("""Soy un apasionado de la tecnología aplicada a los sistemas de información. Tengo conocimientos en metodologías ágiles Scrum y Kanban. He trabajado en la elaboración
                        de dashboards orientado a resultados . Siempre estoy en búsqueda de la mejora continua y con muy buena capacidad de comunicación en equipos de trabajo.
                        También me desempeño como consultor BI en proyectos FreeLance. Realizo desarrollos en Python, orientado a la resolución de procesos complejos y rutinarios 
                        de manipulación de datos con scripts que permiten optimizar tiempos, reducir ejecuciones y contribuyen a los procesos de ETL.
                        En búsqueda constante de desafíos para potenciar los proyectos que me toquen realizar y generar el mayor valor al producto o negocio.""")
                    , color = styles.color.CONTENT.value
                    ,weight='light'
                    ,text_align = 'justify'
                    ,padding = "30px 0px"
                    ),
                    
                rx.image(src = "DataW.jpg"),
                
                
                rx.heading("""Experiencia Laboral""",
                        size= '5',
                        color = color.Color.PRIMARY.value,
                        high_contrast=True,
                        padding = "30px 0px"
                        ), 
                rx.box(
                    rx.accordion.root(
                            rx.accordion.item(
                                header=rx.text("2024",
                                               color = styles.color.PRIMARY.value),
                                content= rx.text("The first accordion item's content",
                                                 color = styles.color.CONTENT.value),
                                
                            ),
                            rx.accordion.item(
                                header=rx.text("2023",
                                               color = styles.color.PRIMARY.value),
                                content=rx.text("The second accordion item's content",
                                                color = styles.color.CONTENT.value),
                                
                            ),
                            rx.accordion.item(
                                header=rx.text("2022",
                                               color = styles.color.PRIMARY.value),
                                content=rx.text("The third accordion item's content",
                                            color = styles.color.CONTENT.value),
                            ),
                            collapsible = True,
                            type = "multiple",
                            #color_scheme = 'iris'
                            variant="ghost",
                            
                        ),
                )               
            
    )