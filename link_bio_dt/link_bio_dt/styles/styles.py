import reflex as rx
from enum import Enum
from .color import Color as color
from .fonts import Font_text as font

#Constants
MAX_WIDTH = "600px"


#Sizes
class Spacer(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    
        
    
 
#Styles
BASE_STYLE = {
    rx.button: {
        "margin" : "auto",
        "width" : "100%",
        "height" : "100%",     
        }
    ,
    rx.text:{
        "color" : color.CONTENT.value,
        "size" : Spacer.SMALL.value,
        "font_family" : font.FONT_TEXT.value
    
    }
}    
