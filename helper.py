from instabot import Bot
from platform   import system
from glob import glob
from pathlib import Path
from secret import username,password
from Tags import TAGS,CAPTIONS
from numpy.random import choice
from os import makedirs,path,rename
import subprocess
from PIL import Image
from instapy_cli import client
    
def PWD(__file__):
    return str(Path(__file__).parent.absolute()) +"/"

current_dir = PWD(__file__)

def RandomFont():
    fonts = glob(current_dir+"theme/fonts/*.ttf")
    font = choice(fonts)
    return font

def createTags():
    tag = choice(TAGS,7)
    listTotags = ' '.join([str(elem) for elem in tag]) 
    return listTotags

def createCaption():
    return choice(CAPTIONS)

def Ping():
    """
    Returns True if host (str) responds to a ping request.
    """
    param = '-n' if system().lower()=='windows' else '-c'

    command = ['ping', param, '2', "google.co.in"]

    return subprocess.call(command) == 0


# TEXT WRAP
def TextWrap(text, font, max_width):
    lines = []
    current_h= 0.0
    pad=0.0
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
        current_h =max_width * .45
        pad = 45
    else:
        words = text.split(' ')  
        i = 0
        while i < len(words):
            line = ''         
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)
        
        # line 4 = 30 line 5 & 6  25

        current_h = (max_width * .30)
        pad = 10
        
    print("Total Lines == ",len(lines)) 
    return lines,int(current_h),pad

def ReduceOpacity(png, opacity):
    """
    Returns an image with reduced Alpa.
    """
    png.putalpha(opacity)
    png.load() # required for png.split()
    background = Image.new("RGB", png.size, (opacity, opacity, opacity))
    background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
    # background.save(file_path)

    return background
   
    
# UPLOAD IMAGE TO INSTAGRAM
def UploadInsta(file_name):
    bot = Bot() 
    bot.login(username = username,  
            password = password) 
    
    bot.upload_photo(file_name, 
                    caption = createCaption() + "\n \n" +createTags() ) 
    # caption = createCaption() + "\n \n" +createTags()
    # with client(username, password) as cli:
    #     cli.upload(file_name, caption)