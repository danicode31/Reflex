import reflex as rx
import link_bio_dt.styles.styles as styles
import link_bio_dt.styles.color as color

def contenido() -> rx.Component:
    return  rx.box(
                rx.text("""Sobre mi..""",
                        size= '5',
                        color = color.Color.PRIMARY.value),
                        
                
                rx.text("""Soy un apasionado de la tecnología aplicada a los sistemas de información. Tengo conocimientos en metodologías ágiles Scrum y Kanban. He trabajado en la elaboración
                        de dashboards orientado a resultados . Siempre estoy en búsqueda de la mejora continua y con muy buena capacidad de comunicación en equipos de trabajo.
                        También me desempeño como consultor BI en proyectos FreeLance. Realizo desarrollo en Python, orientado a la resolución de procesos complejos y rutinarios 
                        de manipulación de datos con scripts de alto impacto que permiten optimizar tiempos de ejecución y contribuyen ETL.
                        En búsqueda constante de desafíos para potenciar los proyectos que me toquen realizar y generar el mayor valor al producto o al negocio."""
                    , color = styles.color.CONTENT.value
                    ,weight='light'
                    ,text_align = 'justify'
                       
                    
                )
                
                
            
    )