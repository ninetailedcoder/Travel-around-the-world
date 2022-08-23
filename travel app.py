from PIL import Image

me = Image.open('travel photo.png')
bg= Image.open('travel three.jpg')
bg.paste(me, (0, 0), me)
bg.show()