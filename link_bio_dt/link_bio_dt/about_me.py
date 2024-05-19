import reflex as rx
import link_bio_dt.styles.styles as styles
from link_bio_dt.components.text_content import text_title


def about_me() -> rx.Component:
    return rx.box(
        rx.markdown("---"),
        text_title("Sobre mi"),
        rx.box(
            rx.flex(
                rx.vstack(
                    rx.text(
                        "Soy ingeniero de datos y desarrollador ",
                        rx.text.strong("Python"),
                        ", me apasiona utilizar la tecnología para resolver problemas complejos e impulsar el valor empresarial. Aprovecho mi experiencia en herramientas de ingeniería de datos como Teradata y secuencias de comandos Python para automatizar flujos de datos y extraer información valiosa.",
                    ),
                    rx.text(
                        "Además, poseo sólidas habilidades en la suite Business Intelligence de Microsoft (SSIS, SSAS, SSRS) y Power BI, lo que me permite transformar datos sin procesar en informes y paneles procesables."
                    ),
                    rx.text(
                        "Apasionado por la tecnología y su aplicación en sistemas de información, con sólidas habilidades en metodologías ágiles como Scrum y Kanban. Poseo amplia experiencia en la elaboración de dashboards orientados a resultados, impulsando la mejora continua y optimizando procesos."
                    ),
                    rx.text(
                        "Experto en consultoría BI y desarrollo de scripts en Python, enfocado en la resolución de tareas complejas y rutinarias de manipulación de datos. Mis scripts automatizan procesos, reducen tiempos de ejecución y contribuyen a la eficiencia en ETL."
                    ),
                    rx.text(
                        "Comunicador efectivo y colaborador nato, con gran capacidad para trabajar en equipo y aportar valor a los proyectos. Me encuentro en constante búsqueda de desafíos que me permitan incrementar mi potencial y generar un impacto significativo en el producto o negocio."
                    ),
                ),
                padding=styles.Spacing.SMALL.value,
                
            ),
            rx.image(src="DataW.jpg"),
            color=styles.Color.Color.CONTENT.value,
            text_align="justify",
        ),
    )
