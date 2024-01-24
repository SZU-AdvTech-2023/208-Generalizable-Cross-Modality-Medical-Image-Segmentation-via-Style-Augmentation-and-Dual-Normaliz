import numpy as np
import os
from matplotlib import pyplot as plt
sampled_batch = np.load("D:\Target\\tice\\t1ce_ss\sample10448_0.npz")
image = sampled_batch["image"].T
plt.imshow(image, cmap='gray')
plt.show()
