import numpy as np
import matplotlib.pyplot as plt
import urllib.request
from pathlib import Path
from PIL import Image

image_file = Path("ucf_ml.jpg")
if not image_file.is_file():
    urllib.request.urlretrieve("https://www.cs.ucf.edu/wp-content/uploads/2019/08/ucf_80085661_Large-1-1600x500.jpg", filename="ucf_ml.jpg")

im = Image.open('ucf_ml.jpg')
arr = np.array(im)
print(arr.shape)
plt.imshow(arr)
plt.show()

gray = arr.mean(axis=2)
plt.imshow(gray)
plt.show()

gray = arr.mean(axis=2)
plt.imshow(gray, cmap='gray')
plt.show()