from PIL import Image

def compute_pixel_difference(image_a, image_b):

    pixels_a = image_a.load()
    pixels_b = image_b.load()

    width, height = image_a.size

    binary = '0'
    s = []
    count = 0
    for x in range(width):
        for y in range(height):
            r_diff = (pixels_a[x, y][0] - pixels_b[x, y][0])
            g_diff = (pixels_a[x, y][1] - pixels_b[x, y][1])
            b_diff = (pixels_a[x, y][2] - pixels_b[x, y][2])

            if not r_diff+g_diff+b_diff == 0:
                binary += str(r_diff)

    print(binary)
    for i in range(0,len(binary),8):
        print(chr(int(binary[i:i+8],2)),end='')
    print()

if __name__ == "__main__":
    image_a = Image.open('chall1.png')
    image_b = Image.open('cay.png')

    if image_a.size != image_b.size:
        print("Error!")
    else:
        compute_pixel_difference(image_a, image_b)