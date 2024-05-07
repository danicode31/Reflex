import reflex as rx
import link_bio_dt.styles.styles as styles
import link_bio_dt.styles.color as color
from datetime import datetime 

class MomentState(rx.State):
    date_now: datetime = datetime.now()

def contenido() -> rx.Component:
    return  rx.box(
                rx.heading("""Sobre mi""",
                        size= '5',
                        color = color.Color.PRIMARY.value,
                        high_contrast=True,
                        padding = "30px 0px"
                        ),
                rx.box(
                    rx.text("""Soy un apasionado de la tecnología aplicada a los sistemas   de información. Tengo conocimientos en metodologías ágiles Scrum y Kanban. He trabajado en la elaboración
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
                                header=rx.text("03-04-2024 al ",rx.moment(MomentState.date_now, format="DD-MM-YYYY", color = color.Color.PRIMARY.value),
                                               color = styles.color.PRIMARY.value),
                                        
                                content= rx.center(
                                    rx.flex(
                                        rx.text(
                                            """NEORIS""",size='5',color = styles.color.CONTENT.value
                                        ),rx.text(
                                            """ Comencé a trabajar en Neoris el 3 de abril del 2024. Para un proyecto de desacople entre Prisma medios de pago y 3 empresas, en el cual se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server 2019 con la utilización de Microsoft Integration Services. 
                                            """,color = styles.color.CONTENT.value, margin = '10px 0px 0px 0px',size='2', text_align = 'justify'
                                        ),
                                        rx.text(
                                            """ A continuación se listan algunas de las tareas que se realizaron y/o, en las cuales estoy trabajando actualmente.
                                            """,color = styles.color.CONTENT.value, margin = '10px 0px 0px 0px',size='2', text_align = 'justify'
                                        ),
                                        rx.text(
                                            """ • Relevamiento de Server """,color = styles.color.CONTENT.value, margin = '10px 0px 0px 20px',size='1'
                                        ),
                                        rx.text(
                                            """ • Planificación de Desacople """,color = styles.color.CONTENT.value, margin = '10px 0px 0px 20px',size='1'
                                        ),
                                        rx.text(
                                            """ • Modelado de datos para la migración """,color = styles.color.CONTENT.value, margin = '10px 0px 0px 20px',size='1'
                                        ),
                                        rx.text(
                                            """ • Pruebas para la migración """,color = styles.color.CONTENT.value, margin = '10px 0px 0px 20px',size='1'
                                        ),
                                        rx.text(
                                            """ • Puesta en producción """,color = styles.color.CONTENT.value, margin = '10px 0px 0px 20px',size='1'
                                        ),
                                        rx.text(
                                            """ • Mantenimiento de modelos """,color = styles.color.CONTENT.value, margin = '10px 0px 0px 20px',size='1'
                                        ),
                                        direction="column",
                                        spacing="4",
                                    ),
                                    
                                )
                            ),
                            rx.accordion.item(
                                header=rx.text("2023 - 2024",
                                               color = styles.color.PRIMARY.value),
                                content=rx.text("The second accordion item's content",
                                                color = styles.color.CONTENT.value),
                                
                            ),
                            rx.accordion.item(
                                header=rx.text("2020 - 2023",
                                               color = styles.color.PRIMARY.value),
                                content=rx.text("The third accordion item's content",
                                            color = styles.color.CONTENT.value),
                            ),
                             rx.accordion.item(
                                header=rx.text("2017 - 2019",
                                               color = styles.color.PRIMARY.value),
                                content=rx.text("The third accordion item's content",
                                            color = styles.color.CONTENT.value),
                            ),
                              rx.accordion.item(
                                header=rx.text("2015 - 2016",
                                               color = styles.color.PRIMARY.value),
                                content=rx.text("The third accordion item's content",
                                            color = styles.color.CONTENT.value),
                            ),
                               rx.accordion.item(
                                header=rx.text("2010 - 2014",
                                               color = styles.color.PRIMARY.value),
                                content=rx.text("The third accordion item's content",
                                            color = styles.color.CONTENT.value),
                                
                                
                            ),
                            collapsible = True,
                            type = "multiple",
                            #color_scheme = 'iris',
                            variant="ghost",
                            orientation = 'vertical',
                            dir = 'ltr'
                        ),
                )               
            
    )