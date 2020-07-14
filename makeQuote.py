from PIL import Image,ImageDraw
from configVars import AUTHOR,MAX_H,MAX_W,FONT,FONT_SIGN,SIGN_TXT
from numpy import mean
from imageio import imread
from borderDesign import CrisCrossRect
from helper import PWD
class QuoteImg:
    def __init__(self):
        pass

    def isBgLight(self,img, thrshld):
        is_light = mean(img) > thrshld
        return "#000000" if is_light else "#ffffff" 

    def  writeImg(self,quoteWrap,alpha_img,txtColor):

        # img_open = Image.open(file_path)
        draw = ImageDraw.Draw(alpha_img)
        current_h = quoteWrap[1]
        pad = quoteWrap[2]

        # WRITE ON IMAGE
        print("WRITE ON IMAGE")
        for line in quoteWrap[0]:

            w, h = draw.textsize(line, font=FONT)
            draw.text(((MAX_W - w) / 2, current_h), line, font=FONT,fill=txtColor)
            current_h += h + pad

        # Write Author and insta ID
        w1,h1 = draw.textsize(AUTHOR, font=FONT_SIGN)
        w2,h2 = draw.textsize(SIGN_TXT, font=FONT_SIGN)
        draw.text(((MAX_W - w1) /2 , (MAX_H - 100)), AUTHOR,font= FONT_SIGN , fill=txtColor)
        draw.text(((MAX_W - w2 ) /2 , (MAX_H - 70)), SIGN_TXT,font= FONT_SIGN , fill=txtColor)
        CrisCrossRect(draw,txtColor)

        saved_file_path = PWD(__file__)+"quotesImg/currentQuote.jpg"
        alpha_img.save(saved_file_path)
        
        return saved_file_path


    def quoteOnImg(self,quoteWrap,alpha_img):

        # img_color = imread(alpha_img,as_gray=True)
        img_color = alpha_img.convert('LA')
        txtColor = self.isBgLight(img_color,190)
        # txtColor = "#ffffff"
        
        print('txtColor',alpha_img,txtColor)
        saved_file= self.writeImg(quoteWrap,alpha_img,txtColor)
        return saved_file
        # self.CrisCrossRect(draw,currentTheme)
