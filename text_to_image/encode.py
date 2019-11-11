import sys
from PIL import Image
def encode_image(img, msg):

    length = len(msg)
    # limit length of message to 255
    if length > 255:
        print("text too long! (don't exeed 255 characters)")
        return False
    if img.mode != 'RGB':
        print("image mode needs to be RGB")
        return False

    encoded = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                c = msg[index -1]
                asc = ord(c)
            else:
                asc = r
            encoded.putpixel((col, row), (asc, g , b))
            index += 1
    return encoded


original_image_file = sys.argv[1]
img = Image.open(original_image_file)
# image mode needs to be 'RGB'
print(img, img.mode)  # test
# create a new filename for the modified/encoded image
encoded_image_file = "enc_" + original_image_file
# don't exceed 255 characters in the message
print("Enter a small secret message: ")
secret_msg = input()
print("len of secret message", len(secret_msg))
img_encoded = encode_image(img, secret_msg)

if img_encoded:
    img_encoded.save(encoded_image_file)
    print("{} saved!".format(encoded_image_file))
else:
    print("Error encoding!")
