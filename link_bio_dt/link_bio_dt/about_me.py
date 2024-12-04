import reflex as rx
import link_bio_dt.styles.styles as styles
from link_bio_dt.components.text_content import text_title


def about_me(title: str) -> rx.Component:
    return rx.vstack(
        text_title(title),
        rx.flex(
            rx.vstack(
                rx.text(
                    "Soy ",
                    rx.text.strong("Data Engineer"),
                    " y desarrollador ",
                    rx.text.strong("Python"),
                    ", me apasiona utilizar la tecnología para resolver problemas complejos e impulsar el valor empresarial. Aprovecho mi experiencia en herramientas de ingeniería de datos como Teradata y secuencias de comandos Python para automatizar flujos de datos y extraer información valiosa.",
                size='4'),
                rx.text(
                    "Además, poseo sólidas habilidades en la suite Business Intelligence de Microsoft (SSIS, SSAS, SSRS) y Power BI, lo que me permite transformar datos sin procesar en informes y dashboards dinámicos.",
                size='4'),
                rx.spacer(),
                rx.image(
                    src="DataW.WebP",
                    loading="lazy",
                    alt="Data WareHouse",
                    min_width="250px",
                    border_color=styles.Color.Color.CONTENT.value,
                ),
                rx.spacer(),
                rx.text(
                    "Soy un apasionado de la tecnología y la transformación digital, con un sólido historial en la implementación de soluciones de BI y automatización. Mis habilidades en metodologías ágiles y herramientas de visualización de datos me permiten traducir información compleja en insights accionables, impulsando la toma de decisiones estratégicas.",
                size='4'
                ),
                rx.text(
                    "Por otro lado, como consultor BI proactivo, me apasiona ayudar a las organizaciones a aprovechar al máximo sus datos. Combino mi expertise en Python + IA junto con metodologías ágiles, para diseñar e implementar soluciones de Business Intelligence innovadoras que generan un valor agregado. Me esfuerzo por encontrar soluciones efectivas a los desafíos de los clientes, siempre buscando oportunidades para optimizar procesos y mejorar los resultados.",
                size='4'
                ),
                rx.text(
                    "Colaboro de manera fluida en equipos multidisciplinarios, aportando mi capacidad de comunicación y mi enfoque en la resolución de problemas. Soy un apasionado del trabajo en equipo y busco constantemente oportunidades para desarrollar nuevas habilidades y generar un impacto significativo en los proyectos.",
                size='4'
                ),
            ),
            padding=styles.Spacing.SMALL.value,
        ),
        color=styles.Color.Color.CONTENT.value,
        align_content="center",
    )
