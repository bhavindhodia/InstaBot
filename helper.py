from instabot import Bot
import platform    
import subprocess 
import pathlib
from secret import username,password

def PWD(__file__):
    return str(pathlib.Path(__file__).parent.absolute())

current_dir = PWD(__file__)

def Ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '3', host]

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
    print("Line",len(lines)) 
    return lines,int(current_h),pad

# UPLOAD IMAGE TO INSTAGRAM
def UploadInsta(file_name):
    bot = Bot() 
    bot.login(username = username,  
            password = password) 
    print("success")
    # bot.upload_photo(current_dir+'/quotesImg/'+file_name, 
    #                 caption ="Daily Quote 😇") 