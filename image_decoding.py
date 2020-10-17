from PIL import Image
im = Image.open("imageEmbedded.png")
theimage = im.load()
width, height = im.size
for x in range(width):
    for y in range(height):
        (r, g, b) = theimage[x, y]
        if (r, g, b) < (2, 2, 2):
            theimage[x, y] = (255, 255, 255)

im.save("imageanswer.png")