from PIL import Image

#pastes one file photo onto another 

#edit variables me and bg to the name of your files 
me = Image.open('')
bg= Image.open('')
bg.paste(me, (0, 0), me)
bg.show()