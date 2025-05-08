from PIL import Image, ImageDraw, ImageFont
import os

# Create a blank image with a white background
img = Image.new('RGBA', (256, 256), color=(255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Draw a blue circle as background
draw.ellipse((20, 20, 236, 236), fill=(0, 120, 212, 255))

# Draw text on the image
try:
    # Try to load a font, fall back to default if not available
    font = ImageFont.truetype("arial.ttf", 100)
except IOError:
    font = ImageFont.load_default()

# Draw "OT" text in white
draw.text((85, 75), "OT", fill=(255, 255, 255, 255), font=font)

# Save the image as ICO file
img.save('icon.ico', format='ICO')
print("Icon created successfully!")
