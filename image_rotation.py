
# First flip the image horizontally, row [0, 1, 1] becomes [1, 1, 0]
# Then invert the image, row [1, 1, 0] becomes [0, 0, 1]

# 0, 1, 2
# 0, 1, 2, 3

def rotate_image(image_arr):
    for row in image_arr:
        right = len(row) - 1
        for i in range(len(row)//2):
            row[i], row[right - i] = row[right - i], row[i]
    for row in image_arr:
        for i in range(len(row)):
            row[i] ^= 1
    return image_arr


if __name__ == "__main__":
    input_arr = [[1, 0, 1], [1, 1, 1], [0, 1, 1]]
    print(rotate_image(input_arr))

