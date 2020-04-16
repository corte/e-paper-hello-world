import lib.epd7in5bc as epd7in5bc
from PIL import Image, ImageDraw
import time

epd = epd7in5bc.EPD() # get the display

def printToDisplay():
    print("Writing to screen...")
    
    HBlackImage = Image.open("./images/black.bmp")
    HRedImage = Image.open("./images/red.bmp")

    epd.display(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))

    time.sleep(2)

try:
    epd.init()
    print("Clearing screen...")
    epd.Clear()
    time.sleep(1)

    printToDisplay()

except IOError as e:
    print(e)

except KeyboardInterrupt:    
    print(" - ctrl + c:")
    epd7in5bc.epdconfig.module_exit()
    exit()