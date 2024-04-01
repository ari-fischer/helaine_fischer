from pdf2image import convert_from_path

# Path to your PDF file
pdf_path = 'Perception_one.pdf'

# Convert PDF to list of images
images = convert_from_path(pdf_path)

# Save each page as an image
for i, image in enumerate(images):
    image.save(f'page_{i + 1}.png', 'PNG')