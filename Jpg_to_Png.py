from PIL import Image
import os

def convert_jpg_to_png(input_folder, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            # Open the image
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            
            # Convert to PNG format
            new_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_folder, new_filename)
            img.save(output_path, "PNG")
            
            print(f"Converted {filename} to {new_filename}")

# Example usage
input_folder = "C:/Users\Sort/Desktop/JPG"
output_folder = "C:/Users/Sort/Desktop/PNG"
convert_jpg_to_png(input_folder, output_folder)
