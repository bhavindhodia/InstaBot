from helper import PWD ,RandomFont
from PIL import ImageFont


FONT = ImageFont.truetype(RandomFont(), 40)
MAX_W, MAX_H = 720,720
QUOTE_WRAP_SIZE = 575
AUTHOR = "By PepperI"
SIGN_TXT = "@ai2motivate"
FONT = ImageFont.truetype(RandomFont(), 40)
FONT_SIGN = ImageFont.truetype(
    PWD(__file__)+'theme/fonts/merriweatherRegular.ttf', 25)

