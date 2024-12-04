import reflex as rx
import link_bio_dt.styles.styles as styles
import link_bio_dt.styles.color as color
import link_bio_dt.constants as constants
from link_bio_dt.components.link_title import link_title
from link_bio_dt.components.text_content import (
    text_content,
    text_title,
    tecno_utils,
    text_content_item,
)


def jobs(title: str) -> rx.Component:
    return (
        rx.box(text_title(title)),
        rx.flex(
            rx.vstack(
                rx.box(
                    rx.image(
                        src="/ia.WebP",
                        margin_y="20px",
                        min_width="250px",
                    )
                ),
                rx.accordion.root(
                    rx.accordion.item(
                        # NEORIS
                        header=rx.heading(
                            "Actualmente", color=color.TextColor.HEADER.value, size="6"
                        ),
                        content=rx.flex(
                            link_title("Neoris", "neoris_logo.WebP", constants.NEORIS),
                            rx.heading("Data Engineer",size='8'),
                            text_content("Ingreso:  3 de abril del 2024"),
                            rx.spacer(),
                            text_content(
                                "Me sumé al equipo de Neoris para un proyecto ambicioso de desacople entre Prisma medios de pago y tres empresas que buscan sectorizar la gestión de los medios de pagos electrónicos."
                            ),
                            rx.spacer(),
                            text_content(
                                "Se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server con la utilización de Microsoft Integration Services."
                            ),
                            rx.spacer(),
                            text_content("Tareas Realizadas:"),
                            text_content_item(
                                "Relevamiento y análisis de los requerimientos de negocio"
                            ),
                            text_content_item("Interacción con usuarios claves"),
                            text_content_item(
                                "Análisis de Jobs, pre y post - condiciones"
                            ),
                            text_content_item(
                                "Diseño y creación de nuevos procesos de ETL con SSIS"
                            ),
                            text_content_item("Análisis y diseño del modelo de datos"),
                            text_content_item(
                                "Mapeo de servidores e infraestructura a desacoplar"
                            ),
                            text_content_item("Mantenimiento de modelos"),
                            rx.text(
                                tecno_utils(constants.TECNOLOGIAS_NEORIS), align="right"
                            ),
                            direction="column",
                            spacing="4",
                            padding=styles.Spacing.SMALL.value,
                            bg=color.Color.SECONDARY.value,
                        ),
                    ),
                    # CDA Informática
                    rx.accordion.item(
                        header=rx.heading(
                            "2023 - 2024", color=color.TextColor.HEADER.value, size="6"
                        ),
                        content=rx.flex(
                            link_title(
                                "CDA Informática",
                                "cda_informatica_logo.WebP",
                                constants.CDA,
                            ),
                            rx.heading("Data Engineer",size='8'),
                            rx.flex(
                                rx.vstack(
                                    text_content("Ingreso: 4 de Septiembre de 2023"),
                                    rx.spacer(),
                                    text_content(
                                        'Este cambio marcó un hito en mi trayectoria profesional, pues dejé atrás 13 años de crecimiento constante en Codere para embarcarme en una nueva experiencia en el sector bancario. Durante 6 meses, formé parte del Banco Galicia, donde integré el equipo de Incentivos, también conocido como "Squad Incentivos". Esta experiencia me brindó la oportunidad de adquirir un profundo conocimiento sobre el negocio y la dinámica del equipo.'
                                    ),
                                    rx.spacer(),
                                    text_content(
                                        "Durante mi experiencia en esta empresa, tuve la oportunidad de participar en proyectos de migración y desarrollo de nuevos indicadores, respondiendo a las necesidades específicas del negocio. Esta experiencia me brindó un aprendizaje invaluable y me permitió conocer a personas excepcionales, altamente comprometidas con su trabajo y con una gran ética profesional."
                                    ),
                                ),
                                direction="column",
                                spacing="4",
                            ),
                            text_content("Tareas Realizadas:"),
                            rx.spacer(),
                            text_content_item(
                                "Análisis de los requerimientos de negocio"
                            ),
                            text_content_item(
                                "Desarrollo de Store Procedures (según reglas de negocio)"
                            ),
                            text_content_item("Monitoreo con Control – M"),
                            text_content_item(
                                "Incidentes y cancelaciones, relanzamiento de jobs"
                            ),
                            text_content_item(
                                "Análisis y corrección de incidentes relevados por el negocio"
                            ),
                            text_content_item("Desarrollo de Dashboard en RP y PBI"),
                            text_content_item("Reuniones de entendimiento de negocio"),
                            text_content_item(
                                "Desarrollos de nuevos indicadores y mantenimiento"
                            ),
                            text_content_item(
                                "Migración de tableros de PBI a Power BI cloud"
                            ),
                            rx.text(
                                tecno_utils(constants.TECNOLOGIAS_CDA), align="right"
                            ),
                            direction="column",
                            spacing="4",
                            margin=styles.Spacing.SMALL.value,
                            padding=styles.Spacing.DEFAULT.value,
                            bg=color.Color.SECONDARY.value,
                        ),
                    ),
                    # CODERE BI
                    rx.accordion.item(
                        header=rx.heading(
                            "2020 - 2023", color=color.TextColor.HEADER.value, size="6"
                        ),
                        content=rx.center(
                            rx.flex(
                                link_title(
                                    "Codere", "codere_logo.WebP", constants.CODERE
                                ),
                                rx.heading("Business Intelligence",size='8'),
                                rx.flex(
                                    rx.vstack(
                                        text_content("Ingreso: 6 de Enero de 2020"),
                                        rx.spacer(),
                                        text_content(
                                            "Este trabajo marcó el inicio de mi carrera profesional en el área de IT, culminando así mi preparación iniciada en el año 2018. Dentro de Codere, tuve la oportunidad de integrarme al Departamento de Soporte Técnico de Sistemas (DTS)."
                                        ),
                                        rx.spacer(),
                                        text_content(
                                            "Posteriormente, gracias a una búsqueda interna y al apoyo de excelentes personas que confiaron en mis capacidades, me incorporé al área de BI. Durante tres años, adquirí valiosos aprendizajes y gané la confianza que me permitió continuar creciendo y afrontar nuevos desafíos."
                                        ),
                                    ),
                                    direction="column",
                                    spacing="4",
                                ),
                                text_content(""" Tareas Realizadas:"""),
                                rx.spacer(),
                                text_content_item(
                                    "Análisis de los requerimientos de negocio"
                                ),
                                text_content_item(
                                    "Desarrollo de Reportes diarios en PBI"
                                ),
                                text_content_item(
                                    "Desarrollo de Informes en Reporting Services"
                                ),
                                text_content_item(
                                    "Control diario de datos sensibles a publicar, para Gerencia"
                                ),
                                text_content_item(
                                    "Desarrollos de soluciones con Integration Services"
                                ),
                                text_content_item(
                                    "Seguimiento y corrección de desvios en contadores"
                                ),
                                text_content_item(
                                    "Documentación y mantenimiento de modelos"
                                ),
                                text_content_item(
                                    "Desarrollos en python para procesos de ETL"
                                ),
                                text_content_item(
                                    "Relevamiento de Arquitectura de datos Uruguay"
                                ),
                                text_content_item(
                                    "Desarrollo modelos de datos Uruguay"
                                ),
                                text_content_item(
                                    "Brindé capacitación de Python para ETL"
                                ),
                                rx.text(
                                    tecno_utils(constants.TECNOLOGIAS_CODERE_BI),
                                    align="right",
                                ),
                                direction="column",
                                spacing="4",
                                margin=styles.Spacing.SMALL.value,
                                padding=styles.Spacing.DEFAULT.value,
                                bg=color.Color.SECONDARY.value,
                            ),
                        ),
                    ),
                    # CODERE CONO SUR
                    rx.accordion.item(
                        header=rx.heading(
                            "2017 - 2019", color=color.TextColor.HEADER.value, size="6"
                        ),
                        content=rx.center(
                            rx.flex(
                                link_title(
                                    "Codere", "codere_logo.WebP", constants.CODERE
                                ),
                                rx.heading("Analista de CI - Cono Sur",size='8'),
                                rx.flex(
                                    rx.vstack(
                                        text_content("Ingreso: 01 de Febrero de 2017"),
                                        rx.spacer(),
                                        text_content(
                                            "Desarrollé mi carrera como Analista de Control de Ingresos para Cono Sur (Argentina - Uruguay) en Codere, donde tuve la oportunidad de trabajar en un equipo altamente comprometido y con una excelente disposición para el trabajo en equipo."
                                        ),
                                        rx.spacer(),
                                        text_content(
                                            "Mi responsabilidad principal era supervisar y controlar las operaciones de cuatro salas de juego, implementando un sistema de seguimiento y monitoreo de eventos que podían indicar potenciales pérdidas para la empresa."
                                        ),
                                    ),
                                    direction="column",
                                    spacing="4",
                                ),
                                text_content(""" Tareas Realizadas:"""),
                                rx.spacer(),
                                text_content_item("Análisis de volumen de juego"),
                                text_content_item("Control de eventos y alertas"),
                                text_content_item("Informes de evolución"),
                                text_content_item(
                                    "Presentación de cierres acumulados mensuales"
                                ),
                                text_content_item("Capacitaciones"),
                                text_content_item("Control de Informes Técnicos"),
                                text_content_item(
                                    "Interacción con las salas y sus Gerentes"
                                ),
                                text_content_item(
                                    "Guardias los fines de semana - Rotativos"
                                ),
                                rx.text(
                                    tecno_utils(constants.TECNOLOGIAS_CODERE_CS),
                                    align="right",
                                ),
                                direction="column",
                                spacing="4",
                                margin=styles.Spacing.SMALL.value,
                                padding=styles.Spacing.DEFAULT.value,
                                bg=color.Color.SECONDARY.value,
                            ),
                        ),
                    ),
                    # CODERE CONCILIACIONES
                    rx.accordion.item(
                        header=rx.heading(
                            "2015 - 2016", color=color.TextColor.HEADER.value, size="6"
                        ),
                        content=rx.center(
                            rx.flex(
                                link_title(
                                    "Codere", "codere_logo.WebP", constants.CODERE
                                ),
                                rx.heading("Analista de PO",size='8'),
                                rx.flex(
                                    rx.vstack(
                                        text_content("Ingreso: 10 de Agosto de 2015"),
                                        rx.spacer(),
                                        text_content(
                                            "Tras cuatro años y medio de formación en la sala de Lanus, donde adquirí un profundo conocimiento de la operación del juego de azar, me integré al equipo de Planeamiento Operativo a través de una búsqueda interna. En esta nueva posición, asumí la responsabilidad del control de conciliaciones de slots, combatiendo fraudes y manteniendo un estado de alerta constante para supervisar y monitorear 13 salas de juego junto con mi equipo."
                                        ),
                                        rx.spacer(),
                                        text_content(
                                            "Implementamos un riguroso sistema de controles cruzados para verificar la información del sistema contra la recaudación real de las máquinas, garantizando la precisión de los datos y la integridad del proceso."
                                        ),
                                    ),
                                    direction="column",
                                    spacing="4",
                                ),
                                text_content(""" Tareas Realizadas:"""),
                                rx.spacer(),
                                text_content_item("Análisis de ruletas"),
                                text_content_item("Análisis y control de Slots"),
                                text_content_item("Conciliación de ruletas"),
                                text_content_item("Control diario de slots y ruletas"),
                                text_content_item("Control de ATM"),
                                text_content_item(
                                    "Control de Tickets Purchases - emitidos en caja"
                                ),
                                text_content_item(
                                    "Interacción con las salas y sus Jefes de Sala"
                                ),
                                text_content_item(
                                    "Guardias los fines de semana - Rotativos"
                                ),
                                rx.text(
                                    tecno_utils(constants.TECNOLOGIAS_CODERE_PO),
                                    align="right",
                                ),
                                direction="column",
                                spacing="4",
                                margin=styles.Spacing.SMALL.value,
                                padding=styles.Spacing.DEFAULT.value,
                                bg=color.Color.SECONDARY.value,
                            ),
                        ),
                    ),
                    # CODERE SALA LANUS
                    rx.accordion.item(
                        header=rx.heading(
                            "2010 - 2015", color=color.TextColor.HEADER.value, size="6"
                        ),
                        content=rx.center(
                            rx.flex(
                                link_title(
                                    "Codere", "codere_logo.WebP", constants.CODERE
                                ),
                                rx.heading("Asistente de slots",size='8'),
                                rx.flex(
                                    rx.vstack(
                                        text_content("Ingreso: 01 de Marzo de 2010"),
                                        rx.spacer(),
                                        text_content(
                                            "Mi primer trabajo formal lo inicié en la sala de Slots de Lanús, donde mi función principal era brindar cambio y atender las necesidades de los clientes que jugaban en la sala. Poco tiempo después, se me presentó la oportunidad de pasar al área de bingo para familiarizarme con su dinámica y trabajar allí un tiempo."
                                        ),
                                        rx.spacer(),
                                        text_content(
                                            "Reconociendo mi interés en el crecimiento y aprendizaje continuo dentro de la empresa, me invitaron a realizar el Máster para Jefe de Sala. Acepté con entusiasmo, ya que me atraía la idea de ampliar mis conocimientos y asumir nuevas responsabilidades. Durante este programa de capacitación de un año de duración, tuve la oportunidad de adquirir experiencia en todos los puestos de trabajo del bingo."
                                        ),
                                    ),
                                    direction="column",
                                    spacing="4",
                                ),
                                text_content(""" Tareas Realizadas:"""),
                                rx.spacer(),
                                text_content_item("Cambista"),
                                text_content_item("Locución"),
                                text_content_item("Vendedor de Bingo"),
                                text_content_item("Cajero de bingo"),
                                text_content_item("Asistente de slots"),
                                text_content_item("Recaudador"),
                                text_content_item("Asistente de Jefe de Sala"),
                                text_content_item("Servicio y atención a los clientes"),
                                direction="column",
                                spacing="4",
                                margin=styles.Spacing.SMALL.value,
                                padding=styles.Spacing.DEFAULT.value,
                                bg=color.Color.SECONDARY.value,
                            ),
                        ),
                    ),
                    # PASANTIA EPSON
                    rx.accordion.item(
                        header=rx.heading(
                            "2008 - 2009", color=color.TextColor.HEADER.value, size="6"
                        ),
                        content=rx.flex(
                            link_title(
                                "Epson", "epsonamerica_logo.WebP", constants.EPSON
                            ),
                            rx.heading("Técnico Eletrónico - Pasantía",size='8'),
                            direction="column",
                            spacing="4",
                            margin=styles.Spacing.SMALL.value,
                            padding=styles.Spacing.DEFAULT.value,
                            bg=color.Color.SECONDARY.value,
                        ),
                    ),
                    collapsible=True,
                    type="multiple",
                    color_scheme="gold",
                    variant="ghost",
                    bg=color.Color.BGACCORDION.value,
                    width = '100%'
                ),
                align_items="center",
            ),
            justify_content="center",
            margin_y=styles.Spacing.DEFAULT.value,
        ),
    )
