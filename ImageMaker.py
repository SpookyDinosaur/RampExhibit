import sys
import time
import base64
from PIL import Image, ImageDraw, ImageFont

fileLocation = "C:///Users/chris/Downloads/tng/ant.mkv"

uniqueCode = "123abc"

def watchVideo(dir, uniqueCode):
    img = Image.new('RGBA', (200, 60))

    fnt = ImageFont.truetype('C:///Windows/WinSxS/amd64_microsoft-windows-font-truetype-arial_31bf3856ad364e35_10.0.17134.1_none_5803fc87168579d6/Arial.ttf', 72)
    d = ImageDraw.Draw(img)
    d.text((20,20), uniqueCode,font = fnt, fill=(255,255,0))
    print("test  ")

    img.save('C:///Users/Christopher/source/repos/RampSoftware/pil_text.png')




watchVideo(fileLocation, uniqueCode)

print("done")

