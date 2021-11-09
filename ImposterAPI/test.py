from random import randint
from PIL import Image
import numpy as np
import os

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 480, 480

bg = (238, 238, 238)
ol = (0, 0, 0)
yl = (255, 255, 102)
rd = (204, 0, 0)
dk = (randint(0, 256), randint(0, 256), randint(0, 256))
ew = (240, 248, 255)
ey = (0, 0, 0)

Angel_Imposter = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, yl, yl, yl, yl, yl, yl, yl, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, yl, bg, bg, bg, bg, bg, bg, bg, yl, bg, bg, bg, bg, bg, bg, bg, bg],        
        [bg, bg, bg, bg, bg, bg, bg, yl, bg, bg, bg, bg, bg, bg, bg, yl, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, yl, yl, yl, yl, yl, yl, yl, bg, bg, bg, bg, bg, bg, bg, bg, bg],        
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
     
    ]

Basic_Imposter = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
     
    ]    



Devil_Imposter = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, rd, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, rd, bg, bg, bg, rd, rd, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, rd, rd, bg, bg, bg, rd, rd, rd, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, rd, rd, rd, bg, bg, bg, rd, rd, rd, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, rd, rd, rd, bg, bg, bg, rd, rd, rd, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, rd, rd, ol, ol, ol, ol, ol, ol, rd, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, rd, ol, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
     
    ]


CrazyGoggle_Imposter = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, ol, dk, dk, dk, dk, dk, dk, dk, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, dk, dk, dk, dk, dk, dk, dk, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, ol, bg, bg, bg, ol, dk, dk, dk, dk, dk, dk, dk, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, dk, dk, dk, dk, dk, dk, dk, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, dk, dk, dk, dk, dk, dk, dk, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, dk, dk, dk, dk, dk, dk, dk, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
     
    ]

Alien_Imposter = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, ew, ew, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, ey, ew, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
     
    ]


    
a = np.array(Basic_Imposter, dtype=np.uint8)

new_image = Image.fromarray(a)
new_image = new_image.resize(dimensions, resample=0)

new_image.save('fffff.png')
