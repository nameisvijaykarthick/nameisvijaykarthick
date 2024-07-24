import os
import shutil

src = r'E:\Desktop 2\Desktop\New Work Vijaykarthick\New folder\P2\\'
dest = r'E:\Desktop 2\Desktop\New Work Vijaykarthick\New folder\Merge\\'

src_files = os.listdir(src)

for folder in src_files:
    folder_path = os.path.join(src, folder)
    if os.path.isdir(folder_path):  # Check if the item is a folder
        for root, _, files in os.walk(folder_path):
            for file in files:
                img_path = os.path.join(root, file)
                shutil.move(img_path, dest)
