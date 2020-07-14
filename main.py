from getQuotes import Quote
from getBG import BgImage
from makeQuote import QuoteImg
from helper import Ping,UploadInsta
from sys import exit
from PIL.ImageDraw import Draw,Image


def RunJob():

    """ If Internet then run """

    if Ping():
        QUOTE = Quote()
        BG_IMG = BgImage()
        QUOTE_IMG = QuoteImg()

        
        quoteis = QUOTE.quoteLines()
        alpha_img = BG_IMG.getBgImg()
        # the_Img = Image.open(temp_Img)
        # bg_img = Draw(alpha_img)
        saved_file =QUOTE_IMG.quoteOnImg(quoteis,alpha_img)
        UploadInsta(saved_file)

        # MakeQuote(quoteis,bgImg)
        

    else:
        exit()

if __name__ == "__main__":
    RunJob()
else:
    print("Else Loop")