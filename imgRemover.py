from rembg import remove

with open("image-cool.jpg", "rb") as i:
    input_img = i.read()

    output = remove(input_img)

with open("no-bg.png", "wb") as o:
    o.write(output)