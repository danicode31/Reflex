import reflex as rx
import link_bio_dt.styles.styles as styles
import link_bio_dt.styles.color as color


def header() -> rx.Component:
    return rx.vstack(
        rx.desktop_only(
            rx.box(
                rx.center(
                    rx.flex(
                        rx.image(
                            src="perfil.WebP",
                            width="150px",
                            heigth="150px",
                            border_radius="100%",
                            alt="perfil",
                            margin_y=styles.Spacing.DEFAULT.value,
                            align="right",
                            loading="lazy",
                        ),
                        rx.vstack(
                            rx.heading(
                                "Daniel Taboada",
                                font_family=styles.Font.TITLE,
                                size="9",
                                color=color.Color.CONTENT.value,
                                text_align="center",
                                margin=styles.Spacing.VERY_SMALL.value,
                                align_content="center",
                                justify_items="center",
                            ),
                            margin_y=styles.Spacing.BIG.value,
                            margin_x=styles.Spacing.LARGE.value,
                            width="auto",
                            box_shadow="-10px -10px #0073b0",
                            border="2px solid",
                            border_color="#0073b0",
                            background_color="#2f4a6577",
                            text_shadow="2px 2px 5px",
                            align_items="center",
                            align_content="center",
                        ),
                        justify_content="center",
                        align="center",
                    ),
                ),
                rx.blockquote(
                    """Data Engineer | Python developer | Digital Transformer | Teradata | AI Enthusiast | Student in Information Technology Management""",
                    color=styles.Color.Color.CONTENT.value,
                    text_align="justify",
                    size="5"                   
                    
                ),
                
            ),
            
        ),
        rx.mobile_and_tablet(
            rx.box(
                rx.center(
                    rx.flex(
                        rx.image(
                            src="perfil.WebP",
                            width="120px",
                            heigth="120px",
                            border_radius="100%",
                            alt="perfil",
                            margin_y=styles.Spacing.DEFAULT.value,
                            align="right",
                            loading="lazy",
                        ),
                        rx.vstack(
                            rx.heading(
                                "Daniel Taboada",
                                font_family=styles.Font.TITLE,
                                size="8",
                                color=color.Color.CONTENT.value,
                                align="center",
                            ),
                            margin_y=styles.Spacing.BIG.value,
                            margin_x=styles.Spacing.LARGE.value,
                            width="auto",
                            box_shadow="-10px -10px #0073b0",
                            border="2px solid",
                            border_color="#0073b0",
                            background_color="#2f4a6577",
                            text_shadow="2px 2px 5px",
                            align_items="center",
                            align_content="center",
                            justify_content="center",
                        ),
                        align="center",
                    ),
                ),
                rx.blockquote(
                    """Data Engineer (Python, Teradata) | Business Intelligence (Power BI, SSIS, SSAS, SSRS) | Digital Transformation Enthusiast | Information Technology Management Student""",
                    color=styles.Color.Color.CONTENT.value,
                    text_align="justify",
                ),
            )
        ),
    )
