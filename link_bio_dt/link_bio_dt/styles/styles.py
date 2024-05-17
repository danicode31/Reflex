import reflex as rx
import reflex as rx
from enum import Enum
import link_bio_dt.styles.color as Color
from .fonts import Font, FontWeight

#Constants
MAX_WIDTH = "600px"


#Sizes

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "/css/styles.css"
]

class Size(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"
    


class Spacing(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
        
    
 
#Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.Color.BACKGROUND.value,
    rx.heading: {
        "color": Color.TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": Color.TextColor.HEADER.value,
        "background_color": Color.Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": Color.Color.SECONDARY.value
        }
    },
    rx.link: {
        "color": Color.Color.PRIMARY.value,
        "text_decoration": "none",
        "_hover": {}
    }
}

# navbar_title_style = dict(
#     font_family=Font.LOGO.value,
#     font_weight=FontWeight.MEDIUM.value,
#     font_size=Size.LARGE.value
# )

# title_style = dict(
#     width="100%",
#     padding_top=Size.DEFAULT.value,
#     font_size=Size.LARGE.value
# )

# button_title_style = dict(
#     font_family=Font.TITLE.value,
#     font_weight=FontWeight.MEDIUM.value,
#     color=Color.HEADER.value,
# )

# button_body_style = dict(
#     font_weight=FontWeight.LIGHT.value,
#     color=Color.BODY.value
# )