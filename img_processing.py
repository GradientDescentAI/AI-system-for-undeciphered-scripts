import cv2
import glob
import os

# Folder with extracted pages
input_folder = "pages_raw/signs"
output_folder = "pages_raw/signs/preprocessed"
os.makedirs(output_folder, exist_ok=True)

# Get all jpg files in order
page_files = sorted(glob.glob(f"{input_folder}/*.jpg"))

for page_path in page_files:
    # Load
    img = cv2.imread(page_path)
    if img is None:
        print(f"Could not read {page_path}, skipping")
        continue

    # Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binarize (invert so lines are black)
    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Save preprocessed
    base_name = os.path.basename(page_path)
    save_path = os.path.join(output_folder, base_name.replace(".jpg", "_preprocessed.png"))
    cv2.imwrite(save_path, bw)

    print(f"Preprocessed {page_path} → {save_path}")
