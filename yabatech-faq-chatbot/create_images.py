from PIL import Image

# Create a dummy logo image
img_logo = Image.new('RGB', (100, 100), color = 'white')
img_logo.save('assets/logo.png')

# Create a dummy background image
img_bg = Image.new('RGB', (800, 600), color = 'grey')
img_bg.save('assets/yabatech.jpg')

print("Dummy images created successfully.")
