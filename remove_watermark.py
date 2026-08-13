"""Remove the 'Dusk · Drift' micro-text from the generated fisheye image.

The text sits in the dark matte below the circle, so we reconstruct that
patch by interpolating the surrounding matte and re-adding matching grain.
"""
import numpy as np
from PIL import Image

SRC = r"C:\Users\84583\AppData\Local\Temp\kimi-desktop-attachments\1786620138145-1-image.png"
DST = r"C:\Users\84583\Desktop\fisheye-retro-v1\dusk-drift-clean.png"

# Patch bounds (original 2048x2048 coords), with margin around the text.
X0, X1 = 855, 1205
Y0, Y1 = 1890, 2020

img = np.asarray(Image.open(SRC).convert("RGB")).astype(np.float64)
h, w, _ = img.shape

# Reference ring around the patch for color/grain statistics.
m = 25
ring = np.concatenate([
    img[Y0 - m:Y0, X0 - m:X1 + m].reshape(-1, 3),
    img[Y1:Y1 + m, X0 - m:X1 + m].reshape(-1, 3),
    img[Y0:Y1, X0 - m:X0].reshape(-1, 3),
    img[Y0:Y1, X1:X1 + m].reshape(-1, 3),
])
noise_sigma = ring.std(axis=0)

# Reconstruct the patch: per-row horizontal interpolation between the matte
# columns just left and right of the patch (the matte is smooth vertically).
patch_h, patch_w = Y1 - Y0, X1 - X0
left = img[Y0:Y1, X0 - 3:X0].mean(axis=1)    # (patch_h, 3)
right = img[Y0:Y1, X1:X1 + 3].mean(axis=1)   # (patch_h, 3)
t = np.linspace(0, 1, patch_w)[None, :, None]
fill = left[:, None, :] * (1 - t) + right[:, None, :] * t

# Feather the patch edges into the original image.
feather = 12
alpha = np.ones((patch_h, patch_w, 1))
ramp = np.linspace(0, 1, feather)
alpha[:feather] *= ramp[:, None, None]
alpha[-feather:] *= ramp[::-1][:, None, None]
alpha[:, :feather] *= ramp[None, :, None]
alpha[:, -feather:] *= ramp[::-1][None, :, None]

rng = np.random.default_rng(7)
grain = rng.normal(0, noise_sigma, size=(patch_h, patch_w, 3))
orig = img[Y0:Y1, X0:X1]
img[Y0:Y1, X0:X1] = np.clip(orig * (1 - alpha) + (fill + grain) * alpha, 0, 255)

Image.fromarray(img.astype(np.uint8)).save(DST)
print("saved:", DST)
