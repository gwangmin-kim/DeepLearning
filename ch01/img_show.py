import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('./img/043.png') # 이미지 읽어오기

plt.imshow(img)
plt.show()