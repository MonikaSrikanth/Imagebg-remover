from rembg import remove
from PIL import Image
img= Image.open('nameLogo.png')
op = remove(img)
op.save('removedbg.png')
op.show()