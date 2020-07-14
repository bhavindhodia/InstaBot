from PIL import Image, ImageDraw, ImageFont,ImageEnhance
from requests import get
from helper import ReduceOpacity,PWD
from io import BytesIO



class BgImage:
    def __init__(self):
        pass

    def getBgImg(self):
        bg_img = get("https://source.unsplash.com/random/720x720/?nature")
        fetched_img =Image.open(BytesIO(bg_img.content))

        png_img_path = PWD(__file__)+"quotesImg/currentQuote.png"
        # fetched_img.save(png_img_path)
        alpha_img =ReduceOpacity(fetched_img, 50) 
        return alpha_img