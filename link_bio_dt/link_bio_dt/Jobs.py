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


def jobs() -> rx.Component:
    return (
        rx.vstack(
            text_title("Experiencia Laboral"),
            rx.accordion.root(
                rx.accordion.item(
                    # NEORIS
                    header=rx.heading(
                        "Actualmente",
                        color=color.TextColor.HEADER.value,
                        size="6",
                        as_="H1",
                    ),
                    content=rx.center(
                        rx.flex(
                            link_title("Neoris", "neoris_logo.jpeg", constants.NEORIS),
                            rx.chakra.heading("Data Engineer"),
                            rx.text(
                                text_content(
                                    "Comencé a trabajar en Neoris el 3 de abril del 2024. Para un proyecto de desacople entre Prisma medios de pago y 3 empresas, en el cual se realizó un trabajo inicial de relevamiento del estado actual y posterioremente se dió inicio al desacople de Teradata hacia SQL Server 2019 con la utilización de Microsoft Integration Services."
                                )
                            ),
                            text_content(""" Tareas Realizadas:"""),
                            text_content_item(
                                "Relevamiento y análisis de los requerimientos de negocio"
                            ),
                            text_content_item("Planificación de Desacople"),
                            text_content_item(
                                "Diseño, creación y mantenimiento del proceso ETL en SSIS y SQL Server"
                            ),
                            text_content_item("Mapeo de datos"),
                            text_content_item("Análisis y diseño del modelo de datos"),
                            text_content_item("Interacción con usuarios claves"),
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
                ),
                # CDA Informática
                rx.accordion.item(
                    header=rx.heading(
                        "2023 - 2024",
                        color=color.TextColor.HEADER.value,
                        size="6",
                        as_="H1",
                    ),
                    content=rx.center(
                        rx.flex(
                            link_title(
                                "CDA Informática",
                                "cda_informatica_logo.jpeg",
                                constants.CDA,
                            ),
                            rx.chakra.heading("Data Engineer"),
                            rx.flex(
                                rx.vstack(
                                    rx.text(
                                        text_content(
                                            "Ingrese a CDA Informática el 4 de Septiembre de 2023. Fue un cambio importante en mi vida profesional ya que luego dejé atrás 13 años de crecimiento continuo en Codere. Para mi fue una experiencia nueva y conocí el core Bancario. Trabajé para el Banco Galicia durante 6 meses. Aprendí muchísimo sobre el negocio y la dinámica que llevaba el equipo o Squad Incentivos como le denominan ellos. "
                                        )
                                    ),
                                    rx.text(
                                        text_content(
                                            "Aquí participé en proyectos de migraciones y desarrollo de nuevos indicadores en funcion a los requerimientos que tenian dentro del negocio. Realmente me llevé una excelente experiencia y tuve la oportunidad de conocer personas excelentes y muy comprometidas con su trabajo."
                                        )
                                    ),
                                ),
                                direction="column",
                                spacing="4",
                            ),
                            rx.text.strong(text_content("Tareas Realizadas:")),
                            text_content_item(
                                "Análisis de los requerimientos de negocio"
                            ),
                            text_content_item(
                                "Desarrollo de Store Procedures (según reglas de negocio)"
                            ),
                            text_content_item("Monitoreo con Control – M"),
                            text_content_item(
                                "Incidentes y cancelacines, relanzamiento de jobs"
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
                ),
                # CODERE BI
                rx.accordion.item(
                    header=rx.heading(
                        "2020 - 2023",
                        color=color.TextColor.HEADER.value,
                        size="6",
                        as_="H1",
                    ),
                    content=rx.center(
                        rx.flex(
                            link_title("Codere", "codere_logo.jpeg", constants.CODERE),
                            rx.chakra.heading("Business Intelligence"),
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
                            margin=styles.Spacing.SMALL.value,
                            padding=styles.Spacing.DEFAULT.value,
                            bg=color.Color.SECONDARY.value,
                        ),
                    ),
                ),
                # CODERE CONO SUR
                rx.accordion.item(
                    header=rx.heading(
                        "2017 - 2019",
                        color=color.TextColor.HEADER.value,
                        size="6",
                        as_="H1",
                    ),
                    content=rx.center(
                        rx.flex(
                            link_title("Codere", "codere_logo.jpeg", constants.CODERE),
                            rx.chakra.heading("Analista de control de ingresos - Cono Sur"),
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
                            margin=styles.Spacing.SMALL.value,
                            padding=styles.Spacing.DEFAULT.value,
                            bg=color.Color.SECONDARY.value,
                        ),
                    ),
                ),
                # CODERE CONCILIACIONES
                rx.accordion.item(
                    header=rx.heading(
                        "2015 - 2016",
                        color=color.TextColor.HEADER.value,
                        size="6",
                        as_="H1",
                    ),
                    content=rx.center(
                        rx.flex(
                            link_title("Codere", "codere_logo.jpeg", constants.CODERE),
                            rx.chakra.heading("Analista de Planeamiento Operativo"),
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
                            margin=styles.Spacing.SMALL.value,
                            padding=styles.Spacing.DEFAULT.value,
                            bg=color.Color.SECONDARY.value,
                        ),
                    ),
                ),
                # CODERE SALA LANUS
                rx.accordion.item(
                    header=rx.heading(
                        "2010 - 2014",
                        color=color.TextColor.HEADER.value,
                        size="6",
                        as_="H1",
                    ),
                    content=rx.center(
                        rx.flex(
                            link_title("Codere", "codere_logo.jpeg", constants.CODERE),
                            rx.chakra.heading("Asistente de slots"),
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
                            margin=styles.Spacing.SMALL.value,
                            padding=styles.Spacing.DEFAULT.value,
                            bg=color.Color.SECONDARY.value,
                        ),
                    ),
                ),
                # PASANTIA EPSON
                rx.accordion.item(
                    header=rx.heading(
                        "2008 - 2009",
                        color=color.TextColor.HEADER.value,
                        size="6",
                        as_="H1",
                    ),
                    content=rx.center(
                        rx.flex(
                            link_title(
                                "Epson", "epsonamerica_logo.jpeg", constants.EPSON
                            ),
                            rx.chakra.heading("Pasantia - Técnico Eletrónico"),
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
                            margin=styles.Spacing.SMALL.value,
                            padding=styles.Spacing.DEFAULT.value,
                            bg=color.Color.SECONDARY.value,
                        ),
                    ),
                ),
                collapsible=True,
                type="multiple",
                color_scheme="gold",
                variant="ghost",
                bg=color.Color.BGACCORDION.value,
            ),
        ),
    )
