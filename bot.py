#! /usr/bin/python
import urllib.request, json ,random
from PIL import Image, ImageDraw, ImageFont
from operator import itemgetter

from types import SimpleNamespace
from helper import TextWrap,UploadInsta,Ping,PWD,RandomFont
from borderDesign import CrisCrossRect
import sys,os,glob


current_dir = PWD(__file__)

# PRE-DEF VARIABLES
MAX_W, MAX_H = 720, 720
AUTHOR = "By PepperI"
SIGN_TXT = "@ai2motivate"
FONT = ImageFont.truetype(RandomFont(), 40)
FONT_SIGN = ImageFont.truetype(
    current_dir+'/'+'/theme/fonts/merriweatherRegular.ttf', 25)



with open(current_dir+'/theme/theme.json') as f:
  themeData = json.load(f)

# print(json.dumps(themeData,indent=2,sort_keys = True))

randomTheme = random.choice(tuple(themeData))
currentTheme = SimpleNamespace(**themeData[randomTheme])
print("Theme  => {0}  == {1} == {2} ".format(currentTheme.textColor,currentTheme.bgColor,RandomFont()))


# GET QUOTE
def getQuote():
    print("FETCHING DATA")
    with urllib.request.urlopen("https://favqs.com/api/qotd") as url:
        data = json.loads(url.read().decode())
        print("DATA FETCHED",data['quote']['body'] )
        
        return data

def MakeQuote():
    quoteData = getQuote()
    txt = quoteData['quote']['body']

    # DRAW IMAGE BASE
    quoteWrap = TextWrap(txt,FONT,512)


    while(len(quoteWrap[0]) >= 7):
        print("\n ******** REFETCHING ******** \n  " )
        quoteData = getQuote()
        txt = quoteData['quote']['body']
        
        quoteWrap = TextWrap(txt,FONT,512)

    print("DRAW IMAGE BG")
    im = Image.new('RGB', (MAX_W, MAX_H), currentTheme.bgColor)
    draw = ImageDraw.Draw(im)
    
    DrawQuote(draw,quoteWrap)

    return im


def DrawQuote(draw,quoteWrap):

    current_h = quoteWrap[1]
    pad = quoteWrap[2]

    # WRITE ON IMAGE
    print("WRITE ON IMAGE")
    for line in quoteWrap[0]:

        w, h = draw.textsize(line, font=FONT)
        draw.text(((MAX_W - w) / 2, current_h), line, font=FONT,fill=currentTheme.textColor)
        current_h += h + pad

    # Write Author and insta ID
    w1,h1 = draw.textsize(AUTHOR, font=FONT_SIGN)
    w2,h2 = draw.textsize(SIGN_TXT, font=FONT_SIGN)
    draw.text(((MAX_W - w1) /2 , (MAX_H - 100)), AUTHOR,font= FONT_SIGN , fill=currentTheme.signColor)
    draw.text(((MAX_W - w2 ) /2 , (MAX_H - 70)), SIGN_TXT,font= FONT_SIGN , fill=currentTheme.signColor)

    CrisCrossRect(draw,currentTheme)

def RunJob():
    if Ping("google.co.in"):
        finalImage = MakeQuote()
        # FILENAME FOR TEMP SAVE
        filename="currentQuote.jpg"

        #SAVE THE FILE
        print("SAVE THE FILE")
        finalImage.save(current_dir+'/quotesImg/'+filename)
        UploadInsta(filename)

    else:
        sys.exit()

RunJob()