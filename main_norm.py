import cv2
import os
import numpy as np

INPUT_DIR = "output/signs"
OUTPUT_DIR = "signs_norm"

CANVAS_SIZE = 64        # final image size
MAX_GLYPH_SIZE = 48     # max width or height inside canvas

os.makedirs(OUTPUT_DIR, exist_ok=True)

for fname in sorted(os.listdir(INPUT_DIR)):
    if not (fname.startswith("sign_") and fname.lower().endswith(".png")):
        continue


    path = os.path.join(INPUT_DIR, fname)
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Skipping unreadable file: {fname}")
        continue

    # --- 1. Binarize ---
    _, bw = cv2.threshold(img, 0, 255,
                           cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Ensure white foreground
    if np.mean(bw) > 127:
        bw = cv2.bitwise_not(bw)

    # --- 2. Tight crop ---
    coords = cv2.findNonZero(bw)
    x, y, w, h = cv2.boundingRect(coords)
    glyph = bw[y:y+h, x:x+w]

    # --- 3. Aspect-ratio resize ---
    h0, w0 = glyph.shape
    scale = MAX_GLYPH_SIZE / max(h0, w0)
    new_w = int(w0 * scale)
    new_h = int(h0 * scale)

    glyph_resized = cv2.resize(
        glyph, (new_w, new_h),
        interpolation=cv2.INTER_NEAREST
    )

    # --- 4. Center on canvas ---
    canvas = np.zeros((CANVAS_SIZE, CANVAS_SIZE), dtype=np.uint8)

    y_off = (CANVAS_SIZE - new_h) // 2
    x_off = (CANVAS_SIZE - new_w) // 2

    canvas[y_off:y_off+new_h, x_off:x_off+new_w] = glyph_resized

    # --- Save ---
    out_path = os.path.join(OUTPUT_DIR, fname)
    cv2.imwrite(out_path, canvas)

print("Normalization complete.")
