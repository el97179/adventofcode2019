import sys
import numpy as np

with open("8") as f:
    input_raw = f.readlines()
input_image = list(filter(lambda i: i.isdigit(), input_raw[0].strip()))

width = 25
height = 6
layers = int(len(input_image) / width / height)
count_0, count_1, count_2 = 0, 0, 0
min_0_layer = sys.maxsize
layer_0, layer_1, layer_2 = [], [], []
image = np.empty(dtype=np.int16, shape=(layers, height, width))
final_image = np.ones(dtype=np.int16, shape=(height, width)) * (-1)
print(final_image)


for k in range(layers):
    count_0, count_1, count_2 = 0, 0, 0
    for i in range(height):
        for j in range(width):
            digit = int(input_image[k*width*height + i*width + j])
            image[k, i, j] = digit
            if digit == 0:
                count_0 += 1
            elif digit == 1:
                count_1 += 1
            elif digit == 2:
                count_2 += 1
    layer_0.append(count_0)
    layer_1.append(count_1)
    layer_2.append(count_2)
    if count_0 < min_0_layer:
        min_0_layer = count_0
        min_0_idx = k
print(f"min_0_idx: {min_0_idx}")
print(f"min_0_layer: {min_0_layer}")
print(f"count_1[min_0_idx]: {layer_1[min_0_idx]}")
print(f"count_2[min_0_idx]: {layer_2[min_0_idx]}")
print(f"result = {layer_1[min_0_idx] * layer_2[min_0_idx]}")

for k in range(layers):
    layer = image[k, :, :]
    idx0 = np.where(layer == 0)
    idx1 = np.where(layer == 1)

    for i in range(height):
        for j in range(width):
            if final_image[i, j] < 0:
                if layer[i, j] != 2:
                    final_image[i, j] = layer[i, j]

print(final_image)