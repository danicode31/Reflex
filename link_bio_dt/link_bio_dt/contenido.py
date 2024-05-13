import reflex as rx
import link_bio_dt.styles.styles as styles
import link_bio_dt.styles.color as color
import link_bio_dt.constants as constants
from link_bio_dt.components.link_title import link_title
from link_bio_dt.components.text_content import text_content
from link_bio_dt.components.text_content import tecno_utils


def contenido() -> rx.Component:
    return  rx.box(
                rx.markdown("---"), 
                rx.chakra.heading("""Sobre mi""",
                        size= 'lg',
                        color = color.Color.PRIMARY.value,
                        padding = "30px 0px",
                        text_shadow = "2px 2px 5px"
                        ),
                rx.box(
                    rx.flex(
                        rx.vstack(
                            rx.text("Soy ingeniero de datos y desarrollador Python, me apasiona utilizar la tecnología para resolver problemas complejos e impulsar el valor empresarial. Aprovecho mi experiencia en herramientas de ingeniería de datos como Teradata y secuencias de comandos Python para automatizar flujos de datos y extraer información valiosa."),
                            rx.text("Además, poseo sólidas habilidades en la suite Business Intelligence de Microsoft (SSIS, SSAS, SSRS) y Power BI, lo que me permite transformar datos sin procesar en informes y paneles procesables."),
                            rx.text("Apasionado por la tecnología y su aplicación en sistemas de información, con sólidas habilidades en metodologías ágiles como Scrum y Kanban. Poseo amplia experiencia en la elaboración de dashboards orientados a resultados, impulsando la mejora continua y optimizando procesos."),
                            rx.text("Experto en consultoría BI y desarrollo de scripts en Python, enfocado en la resolución de tareas complejas y rutinarias de manipulación de datos. Mis scripts automatizan procesos, reducen tiempos de ejecución y contribuyen a la eficiencia en ETL."),
                            rx.text("Comunicador efectivo y colaborador nato, con gran capacidad para trabajar en equipo y aportar valor a los proyectos. Me encuentro en constante búsqueda de desafíos que me permitan incrementar mi potencial y generar un impacto significativo en el producto o negocio."),
                            
                            
                        ),                       
                        padding = '20px'
                    )
                    ,rx.image(src = "DataW.jpg")                    
                    ,color = styles.color.CONTENT.value
                    #,weight='light'
                    ,text_align = 'justify'
                    ),
                                    
                
                rx.chakra.heading("""Experiencia Laboral""",
                        size= 'lg',
                        color = color.Color.PRIMARY.value,
                        high_contrast=True,
                        padding = "30px 0px",
                        text_shadow = "2px 2px 5px"                   
                        ), 
                rx.box(
                    rx.accordion.root(
                            rx.accordion.item(
                                # NEORIS
                                header=rx.chakra.heading("Actualmente",color = styles.color.PRIMARY.value,size='md'),
                                     
                                content= rx.center(
                                    rx.flex(
                                            rx.hstack(rx.image(src="neoris_logo.jpeg",
                                                    width="32px",
                                                    heigth="32px", 
                                                    ),
                                            rx.text(link_title("Neoris",constants.NEORIS)),
                                            
                                        ),
                                        rx.chakra.heading('Data Engineer',size='lg'),
                                        rx.text(text_content("Comencé a trabajar en Neoris el 3 de abril del 2024. Para un proyecto de desacople entre Prisma medios de pago y 3 empresas, en el cual se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server 2019 con la utilización de Microsoft Integration Services.")),
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
                                header=rx.chakra.heading("2023 - 2024",color = styles.color.PRIMARY.value,size='md'),
                                     
                                content= rx.center(
                                    rx.flex(
                                            rx.hstack(rx.image(src="cda_informatica_logo.jpeg",
                                                    width="32px",
                                                    heigth="32px", 
                                                    ),
                                            rx.text(link_title("CDA Informática",constants.CDA)),
                                            

                                        ),
                                        rx.chakra.heading('Data Engineer',size='lg'),
                                        rx.flex(
                                            rx.vstack(
                                                rx.text(text_content("Ingrese a CDA Informática el 4 de Septiembre de 2023. Fue un cambio importante en mi vida profesional ya que luego dejé atrás 13 años de crecimiento continuo en Codere. Para mi fue una experiencia nueva y conocí el core Bancario. Trabajé para el Banco Galicia durante 6 meses. Aprendí muchísimo sobre el negocio y la dinámica que llevaba el equipo o Squad Incentivos como le denominan ellos. ")),
                                                rx.text(text_content("Aquí participé en proyectos de migraciones y desarrollo de nuevos indicadores en funcion a los requerimientos que tenian dentro del negocio. Realmente me llevé una excelente experiencia y tuve la oportunidad de conocer personas excelentes y muy comprometidas con su trabajo.")),
                                            ),
                                            direction="column",
                                            spacing="4",
                                            
                                        )
                                        ,
                                        rx.text.strong(text_content(""" Tareas Realizadas:""")),
                                        rx.text.em(text_content(""" • Análisis de los requerimientos de negocio """)),
                                        rx.text.em(text_content(""" • Desarrollo de Store Procedures (según reglas de negocio) """)),
                                        rx.text.em(text_content(""" • Monitoreo con Control – M """)),
                                        rx.text.em(text_content(""" • Incidentes y cancelacines, relanzamiento de jobs """)),
                                        rx.text.em(text_content(""" • Análisis y corrección de incidentes relevados por el negocio """)),
                                        rx.text.em(text_content(""" • Desarrollo de Dashboard en RP y PBI """)),
                                        rx.text.em(text_content(""" • Reuniones de entendimiento de negocio """)),
                                        rx.text.em(text_content(""" • Desarrollos de nuevos indicadores y mantenimiento """)),
                                        rx.text.em(text_content(""" • Migración de tableros de PBI a Power BI cloud """)),
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
                                header=rx.chakra.heading("2019 - 2023",color = styles.color.PRIMARY.value,size='md'),
                                     
                                content= rx.center(
                                    rx.flex(
                                            rx.hstack(rx.image(src="codere_logo.jpeg",
                                                    width="32px",
                                                    heigth="32px", 
                                                    ),
                                            rx.text(link_title("Codere",constants.CODERE))

                                        ),
                                        rx.chakra.heading('Business Intelligence',size='lg'),
                                        # rx.text(text_content(""" Comencé a trabajar en Neoris el 3 de abril del 2024. Para un proyecto de desacople entre Prisma medios de pago y 3 empresas, en el cual se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server 2019 con la utilización de Microsoft Integration Services.""")),
                                        # rx.text.strong(text_content(""" Tareas Realizadas:""")),
                                        # rx.text.em(text_content(""" • Relevamiento y análisis de los requerimientos de negocio """)),
                                        # rx.text.em(text_content(""" • Planificación de Desacople """)),
                                        # rx.text.em(text_content(""" • Diseño, creación y mantenimiento del proceso ETL en SSIS y SQL Server """)),
                                        # rx.text.em(text_content(""" • Mapeo de datos """)),
                                        # rx.text.em(text_content(""" • Análisis y diseño del modelo de datos """)),
                                        # rx.text.em(text_content(""" • Interacción con usuarios claves """)),
                                        # rx.text.em(text_content(""" • Mantenimiento de modelos """)),
                                        # rx.text(tecno_utils(constants.TECNOLOGIAS_CODERE_BI),align='right'),
                                        
                                        
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
                                header=rx.chakra.heading("2017 - 2019",color = styles.color.PRIMARY.value,size='md'),
                                content=rx.center(
                                    rx.flex(
                                            rx.hstack(rx.image(src="codere_logo.jpeg",
                                                    width="32px",
                                                    heigth="32px", 
                                                    ),
                                            rx.text(link_title("Codere",constants.CODERE))

                                        ),
                                        rx.chakra.heading('Analista de control de ingresos - Cono Sur',size='lg'),
                                        # rx.text(text_content(""" Comencé a trabajar en Neoris el 3 de abril del 2024. Para un proyecto de desacople entre Prisma medios de pago y 3 empresas, en el cual se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server 2019 con la utilización de Microsoft Integration Services.""")),
                                        # rx.text.strong(text_content(""" Tareas Realizadas:""")),
                                        # rx.text.em(text_content(""" • Relevamiento y análisis de los requerimientos de negocio """)),
                                        # rx.text.em(text_content(""" • Planificación de Desacople """)),
                                        # rx.text.em(text_content(""" • Diseño, creación y mantenimiento del proceso ETL en SSIS y SQL Server """)),
                                        # rx.text.em(text_content(""" • Mapeo de datos """)),
                                        # rx.text.em(text_content(""" • Análisis y diseño del modelo de datos """)),
                                        # rx.text.em(text_content(""" • Interacción con usuarios claves """)),
                                        # rx.text.em(text_content(""" • Mantenimiento de modelos """)),
                                        # rx.text(tecno_utils(constants.TECNOLOGIAS_CODERE_BI),align='right'),
                                        
                                        
                                        direction="column",
                                        spacing="4",
                                        margin = styles.Spacer.SMALL.value,
                                        padding = styles.Spacer.DEFAULT.value,
                                        bg = color.Color.SECONDARY.value
                                    ),
                                    
                                )
                            ),
                            # CODERE CONCILIACIONES
                              rx.accordion.item(
                                header=rx.chakra.heading("2015 - 2016",color = styles.color.PRIMARY.value,size='md'),
                                content=rx.center(
                                    rx.flex(
                                            rx.hstack(rx.image(src="codere_logo.jpeg",
                                                    width="32px",
                                                    heigth="32px", 
                                                    ),
                                            rx.text(link_title("Codere",constants.CODERE))

                                        ),
                                        rx.chakra.heading('Analista de Planeamiento Operativo',size='lg'),
                                        # rx.text(text_content(""" Comencé a trabajar en Neoris el 3 de abril del 2024. Para un proyecto de desacople entre Prisma medios de pago y 3 empresas, en el cual se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server 2019 con la utilización de Microsoft Integration Services.""")),
                                        # rx.text.strong(text_content(""" Tareas Realizadas:""")),
                                        # rx.text.em(text_content(""" • Relevamiento y análisis de los requerimientos de negocio """)),
                                        # rx.text.em(text_content(""" • Planificación de Desacople """)),
                                        # rx.text.em(text_content(""" • Diseño, creación y mantenimiento del proceso ETL en SSIS y SQL Server """)),
                                        # rx.text.em(text_content(""" • Mapeo de datos """)),
                                        # rx.text.em(text_content(""" • Análisis y diseño del modelo de datos """)),
                                        # rx.text.em(text_content(""" • Interacción con usuarios claves """)),
                                        # rx.text.em(text_content(""" • Mantenimiento de modelos """)),
                                        # rx.text(tecno_utils(constants.TECNOLOGIAS_CODERE_BI),align='right'),
                                        
                                        
                                        direction="column",
                                        spacing="4",
                                        margin = styles.Spacer.SMALL.value,
                                        padding = styles.Spacer.DEFAULT.value,
                                        bg = color.Color.SECONDARY.value
                                    ),
                                    
                                )
                            ),
                            # CODERE SALA LANUS
                               rx.accordion.item(
                                header=rx.chakra.heading("2010 - 2014",color = styles.color.PRIMARY.value,size='md'),
                                content=rx.center(
                                    rx.flex(
                                            rx.hstack(rx.image(src="codere_logo.jpeg",
                                                    width="32px",
                                                    heigth="32px", 
                                                    ),
                                            rx.text(link_title("Codere",constants.CODERE))

                                        ),
                                        rx.chakra.heading('Asistente de slots',size='lg'),
                                        # rx.text(text_content(""" Comencé a trabajar en Neoris el 3 de abril del 2024. Para un proyecto de desacople entre Prisma medios de pago y 3 empresas, en el cual se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server 2019 con la utilización de Microsoft Integration Services.""")),
                                        # rx.text.strong(text_content(""" Tareas Realizadas:""")),
                                        # rx.text.em(text_content(""" • Relevamiento y análisis de los requerimientos de negocio """)),
                                        # rx.text.em(text_content(""" • Planificación de Desacople """)),
                                        # rx.text.em(text_content(""" • Diseño, creación y mantenimiento del proceso ETL en SSIS y SQL Server """)),
                                        # rx.text.em(text_content(""" • Mapeo de datos """)),
                                        # rx.text.em(text_content(""" • Análisis y diseño del modelo de datos """)),
                                        # rx.text.em(text_content(""" • Interacción con usuarios claves """)),
                                        # rx.text.em(text_content(""" • Mantenimiento de modelos """)),
                                        # rx.text(tecno_utils(constants.TECNOLOGIAS_CODERE_BI),align='right'),
                                        
                                        
                                        direction="column",
                                        spacing="4",
                                        margin = styles.Spacer.SMALL.value,
                                        padding = styles.Spacer.DEFAULT.value,
                                        bg = color.Color.SECONDARY.value
                                    ),
                                    
                                )
                            ),
                            # PASANTIA EPSON
                               rx.accordion.item(
                                header=rx.chakra.heading("2008 - 2009",color = styles.color.PRIMARY.value,size='md'),
                                content=rx.center(
                                    rx.flex(
                                            rx.hstack(rx.image(src="epsonamerica_logo.jpeg",
                                                    width="32px",
                                                    heigth="32px", 
                                                    ),
                                            rx.text(link_title("Epson",constants.EPSON))

                                        ),
                                        rx.chakra.heading('Pasantia - Técnico Eletrónico',size='lg'),
                                        # rx.text(text_content(""" Comencé a trabajar en Neoris el 3 de abril del 2024. Para un proyecto de desacople entre Prisma medios de pago y 3 empresas, en el cual se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server 2019 con la utilización de Microsoft Integration Services.""")),
                                        # rx.text.strong(text_content(""" Tareas Realizadas:""")),
                                        # rx.text.em(text_content(""" • Relevamiento y análisis de los requerimientos de negocio """)),
                                        # rx.text.em(text_content(""" • Planificación de Desacople """)),
                                        # rx.text.em(text_content(""" • Diseño, creación y mantenimiento del proceso ETL en SSIS y SQL Server """)),
                                        # rx.text.em(text_content(""" • Mapeo de datos """)),
                                        # rx.text.em(text_content(""" • Análisis y diseño del modelo de datos """)),
                                        # rx.text.em(text_content(""" • Interacción con usuarios claves """)),
                                        # rx.text.em(text_content(""" • Mantenimiento de modelos """)),
                                        # rx.text(tecno_utils(constants.TECNOLOGIAS_CODERE_BI),align='right'),
                                        
                                        
                                        direction="column",
                                        spacing="4",
                                        margin = styles.Spacer.SMALL.value,
                                        padding = styles.Spacer.DEFAULT.value,
                                        bg = color.Color.SECONDARY.value
                                    ),
                                    
                                )  
                            ),
                            collapsible = True,
                            type = "multiple",
                            color_scheme = 'gold',
                            variant="ghost",
                            orientation = 'vertical',
                            bg = styles.color.BGACCORDION.value
                        ),
                )               
            
    )