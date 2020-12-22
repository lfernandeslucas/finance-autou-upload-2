
image_file = 'local-filename.jpg'

# from PIL import Image
# from IPython.display import Image as img


# image = Image.open('local-filename.jpg')
# image.show()

# display(image)

from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

%matplotlib inline
pil_im = Image.open('image_file', 'r')
imshow(np.asarray(pil_im))