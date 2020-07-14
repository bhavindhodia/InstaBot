
def CrisCrossRect(draw,txtColor):
    #DRAW RECTANGLE
    draw.line((0,20,720,20),fill= txtColor, width=5)
    draw.line((20,720,20,0),fill= txtColor, width=5)
    draw.line((0,700,720,700),fill= txtColor, width=5)
    draw.line((700,720,700,0),fill= txtColor, width=5)
