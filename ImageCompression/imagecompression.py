from PIL import Image
# Open the image
input_image_path = "images.jpg"
image = Image.open('images.jpg') #image name 1.jpg
# Compress and save the image in JPEG format
output_image_path = "Compressed_image.jpg"
image.save(output_image_path, "JPEG", quality=70)
print(f"Compressed image saved as {output_image_path}") 