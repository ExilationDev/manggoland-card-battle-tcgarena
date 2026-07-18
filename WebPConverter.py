import os
from PIL import Image
from tqdm import tqdm


dir_folders = ["./Cards/Objects", "./Cards/Supports", "./Cards/Powers"]
in_folder = "png"
out_folder = "webp"

images_to_convert = []

for f in dir_folders:
    cur_in_folder = os.path.join(f, in_folder)
    cur_out_folder = os.path.join(f, out_folder)
    for filename in os.listdir(cur_in_folder):
        if filename.lower().endswith((".png", ".jpeg", ".jpg")):
            img_path = os.path.join(cur_in_folder, filename)
            images_to_convert.append(img_path)

pbar = tqdm(images_to_convert)
for img_path in pbar:
    pbar.write(f"Converting {img_path} to .webp")
    img = Image.open(img_path)

    output_path = os.path.join(cur_out_folder, f"{os.path.splitext(filename)[0]}.webp")

    img.save(output_path, "WEBP", quality=80)

print(f"Successfully converted all .png images to .webp")
input("Press enter to exit...")
