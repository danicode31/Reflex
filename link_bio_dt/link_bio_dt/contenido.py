import reflex as rx
import link_bio_dt.styles.styles as styles
import link_bio_dt.styles.color as color
import link_bio_dt.constants as constants
from link_bio_dt.components.link_title import link_title
from link_bio_dt.components.text_content import text_content
from link_bio_dt.components.text_content import tecno_utils


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
                                # NEORIS
                                header=rx.text("Actualmente",color = styles.color.PRIMARY.value),
                                     
                                content= rx.center(
                                    rx.flex(
                                            rx.hstack(rx.image(src="neoris_logo.jpeg",
                                                    width="32px",
                                                    heigth="32px", 
                                                    ),
                                            rx.text(link_title("Neoris",constants.NEORIS))

                                        ),
                                        rx.text(text_content(""" Comencé a trabajar en Neoris el 3 de abril del 2024. Para un proyecto de desacople entre Prisma medios de pago y 3 empresas, en el cual se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server 2019 con la utilización de Microsoft Integration Services.""")),
                                        rx.text.strong(text_content(""" Tareas Realizadas:""")),
                                        rx.text.em(text_content(""" • Relevamiento y análisis de los requerimientos de negocio """)),
                                        rx.text.em(text_content(""" • Planificación de Desacople """)),
                                        rx.text.em(text_content(""" • Diseño, creación y mantenimiento del proceso ETL en SSIS y SQL Server """)),
                                        rx.text.em(text_content(""" • Mapeo de datos """)),
                                        rx.text.em(text_content(""" • Análisis y diseño del modelo de datos """)),
                                        rx.text.em(text_content(""" • Interacción con usuarios claves """)),
                                        rx.text.em(text_content(""" • Mantenimiento de modelos """)),
                                        rx.text(tecno_utils(constants.TECNOLOGIAS_NEORIS),align='right'),
                                        
                                        
                                        direction="column",
                                        spacing="4",
                                        margin = styles.Spacer.SMALL.value,
                                        padding = styles.Spacer.DEFAULT.value,
                                        bg = color.Color.SECONDARY.value
                                    ),
                                    
                                )
                            ),
                            # CDA Informática
                            rx.accordion.item(
                                header=rx.text("2023 - 2024",color = styles.color.PRIMARY.value),
                                     
                                content= rx.center(
                                    rx.flex(
                                            rx.hstack(rx.image(src="cda_informatica_logo.jpeg",
                                                    width="32px",
                                                    heigth="32px", 
                                                    ),
                                            rx.text(link_title("CDA Informática",constants.CDA))

                                        ),
                                        rx.text(text_content(""" Comencé a trabajar en Neoris el 3 de abril del 2024. Para un proyecto de desacople entre Prisma medios de pago y 3 empresas, en el cual se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server 2019 con la utilización de Microsoft Integration Services.""")),
                                        rx.text(text_content(""" A continuación se listan algunas de las tareas que se realizaron y/o, en las cuales estoy trabajando actualmente.""")),
                                        rx.text(text_content(""" • Relevamiento y análisis de los requerimientos de negocio """)),
                                        rx.text(text_content(""" • Planificación de Desacople """)),
                                        rx.text(text_content(""" • Diseño, creación y mantenimiento del proceso ETL en SSIS y SQL Server """)),
                                        rx.text(text_content(""" • Mapeo de datos """)),
                                        rx.text(text_content(""" • Análisis y diseño del modelo de datos """)),
                                        rx.text(text_content(""" • Interacción con usuarios claves """)),
                                        rx.text(text_content(""" • Mantenimiento de modelos """)),
                                        rx.text(tecno_utils(constants.TECNOLOGIAS_CDA),align='right'),
                                        
                                        
                                        direction="column",
                                        spacing="4",
                                        margin = styles.Spacer.SMALL.value,
                                        padding = styles.Spacer.DEFAULT.value,
                                        bg = color.Color.SECONDARY.value
                                    ),
                                    
                                )
                                
                            ),
                            # CODERE BI
                            rx.accordion.item(
                                header=rx.text("2020 - 2023",color = styles.color.PRIMARY.value),
                                     
                                content= rx.center(
                                    rx.flex(
                                            rx.hstack(rx.image(src="codere_logo.jpeg",
                                                    width="32px",
                                                    heigth="32px", 
                                                    ),
                                            rx.text(link_title("Codere",constants.CODERE))

                                        ),
                                        rx.text(text_content(""" Comencé a trabajar en Neoris el 3 de abril del 2024. Para un proyecto de desacople entre Prisma medios de pago y 3 empresas, en el cual se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server 2019 con la utilización de Microsoft Integration Services.""")),
                                        rx.text(text_content(""" A continuación se listan algunas de las tareas que se realizaron y/o, en las cuales estoy trabajando actualmente.""")),
                                        rx.text(text_content(""" • Relevamiento y análisis de los requerimientos de negocio """)),
                                        rx.text(text_content(""" • Planificación de Desacople """)),
                                        rx.text(text_content(""" • Diseño, creación y mantenimiento del proceso ETL en SSIS y SQL Server """)),
                                        rx.text(text_content(""" • Mapeo de datos """)),
                                        rx.text(text_content(""" • Análisis y diseño del modelo de datos """)),
                                        rx.text(text_content(""" • Interacción con usuarios claves """)),
                                        rx.text(text_content(""" • Mantenimiento de modelos """)),
                                        rx.text(tecno_utils(constants.TECNOLOGIAS_CODERE_BI),align='right'),
                                        
                                        
                                        direction="column",
                                        spacing="4",
                                        margin = styles.Spacer.SMALL.value,
                                        padding = styles.Spacer.DEFAULT.value,
                                        bg = color.Color.SECONDARY.value
                                    ),
                                    
                                )
                            ),
                            # CODERE CONO SUR
                             rx.accordion.item(
                                header=rx.text("2017 - 2019",
                                               color = styles.color.PRIMARY.value),
                                content=rx.text("The third accordion item's content",
                                            color = styles.color.CONTENT.value),
                            ),
                            # CODERE CONCILIACIONES
                              rx.accordion.item(
                                header=rx.text("2015 - 2016",
                                               color = styles.color.PRIMARY.value),
                                content=rx.text("The third accordion item's content",
                                            color = styles.color.CONTENT.value),
                            ),
                            # CODERE SALA LANUS
                               rx.accordion.item(
                                header=rx.text("2010 - 2014",
                                               color = styles.color.PRIMARY.value),
                                content=rx.text("The third accordion item's content",
                                            color = styles.color.CONTENT.value),
                            ),
                            # PASANTIA EPSON
                               rx.accordion.item(
                                header=rx.text("2008 - 2009",
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