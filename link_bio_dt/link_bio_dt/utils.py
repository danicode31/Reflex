from datetime import datetime, timedelta, timezone

import reflex as rx
import link_bio_dt.styles.color as color

from datetime import datetime


class MomentState(rx.State):
    date_now: datetime = datetime.now()


# rx.moment(MomentState.date_now, format="YYYY-MM-DD", color = color.Color.PRIMARY.value)

# Común


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


# Index

index_title = "Daniel Taboada | CV web"
index_description = (
    "Este es mi CV web y lo comparto para que puedas conocer mis habilidades técnicas."
)


# Date

LOCAL_TIMEZONE_SCRIPT = "Intl.DateTimeFormat().resolvedOptions().timeZone"

WEEKDAYS = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo",
}

MONTHS = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}


