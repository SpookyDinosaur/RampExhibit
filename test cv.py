from PIL import Image, ImageDraw
 
img = Image.new('RGBA', (100, 30))
 
d = ImageDraw.Draw(img)
d.text((10,10), "Hello World", fill=(255,255,0))
 
img.save('pil_text.png')
