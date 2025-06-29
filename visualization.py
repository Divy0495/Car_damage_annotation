import os
import json
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon as MplPolygon

# === Configuration ===
coco_json_path = "annotations/instances_default.json"  # Path to your downloaded file
image_dir = "test"                        # Folder with your images
output_dir = "annotated_outputs"           # Folder to save output images
os.makedirs(output_dir, exist_ok=True)

# === Load JSON ===
with open(coco_json_path, 'r') as f:
    coco = json.load(f)

image_map = {img['id']: img for img in coco['images']}
category_map = {cat['id']: cat['name'] for cat in coco['categories']}

for ann in coco['annotations']:
    img_info = image_map[ann['image_id']]
    img_path = os.path.join(image_dir, img_info['file_name'])

    if not os.path.exists(img_path):
        continue

    img = Image.open(img_path).convert("RGB")
    fig, ax = plt.subplots()
    ax.imshow(img)

    if 'segmentation' in ann:
        for seg in ann['segmentation']:
            x = seg[0::2]
            y = seg[1::2]
            polygon = MplPolygon(list(zip(x, y)), closed=True, edgecolor='red', fill=False, linewidth=2)
            ax.add_patch(polygon)
            ax.text(x[0], y[0]-10, category_map[ann["category_id"]],
                    color="white", fontsize=8, bbox=dict(facecolor="red", alpha=0.5))

    ax.axis("off")
    fig.tight_layout()
    output_path = os.path.join(output_dir, f"annotated_{img_info['file_name']}")
    fig.savefig(output_path)
    plt.close(fig)

print("✅ Saved visualizations to:", output_dir)
