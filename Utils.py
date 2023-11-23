import numpy as np
import cv2

TOTAL_COLOR_VALUE = 256

def extract_power_of_two(number):
    # Find the position of the most significant bit
    power_of_two = number.bit_length() - 1
    return power_of_two

# will create the or mask
def create_masks(power_of_two):
    # Creating OR mask (least significant bits set to 1)
    or_mask = (1 << power_of_two) - 1
    
    return or_mask

# map all pixel values to the higher qunatized value
def high_level_mapping_gray_scale(matrix, quantization_size: int):
    
    #calculate the key
    key = int(TOTAL_COLOR_VALUE / quantization_size)

    power_of_key = extract_power_of_two(key)
    or_mask = create_masks(power_of_key)

    #dimensions of the original matrix
    height = len(matrix)
    width = len(matrix[0])
    # creating new matrix so that original matrix does not gets changed
    new_matrix = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(0, height):
        for j in range(0, width):
            new_matrix[i][j] = int(matrix[i][j]) | or_mask

    return new_matrix


# map all pixel values to the low qunatized value
def low_level_mapping_gray_scale(matrix, quantization_size: int):
    
    #calculate the key
    key = int(TOTAL_COLOR_VALUE / quantization_size)

    # generate range of values according to the key
    power_of_key = extract_power_of_two(key)
    and_mask = ~(create_masks(power_of_key))

    #dimensions of the original matrix
    height = len(matrix)
    width = len(matrix[0])

    new_matrix = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(0, height):
        for j in range(0, width):
            new_matrix[i][j] = int(matrix[i][j]) & and_mask

    return new_matrix

# map all pixel values to the mid qunatized value
def mid_level_mapping_gray_scale(matrix, quantization_size: int):
    
    #calculate the key
    key = int(TOTAL_COLOR_VALUE / quantization_size)

    # generate range of values according to the key
    power_of_key = extract_power_of_two(key)
    or_mask1 = create_masks(power_of_key)

    # calculate mid value
    power_of_key2 = extract_power_of_two(int(key/2))
    and_mask2 = ~(create_masks(power_of_key2))

    #dimensions of the original matrix
    height = len(matrix)
    width = len(matrix[0])

    new_matrix = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(0, height):
        for j in range(0, width):
            matrix_value = int(matrix[i][j]) | or_mask1 # map to higher values
            new_matrix[i][j] = matrix_value & and_mask2

    return new_matrix

# testing matrix
# print(high_level_mapping_gray_scale([[11,32],[128,255]], 4))
# print(low_level_mapping_gray_scale([[11,32],[128,255]], 4))
# print(mid_level_mapping_gray_scale([[11,32],[128,255]], 4))


def mapping_rgb(matrix, quantization_size: int, mapping_level: int):
    #dimensions of the original matrix

    # Extract red, green, and blue channels
    red_matrix = matrix[:, :, 2]
    green_matrix = matrix[:, :, 1]
    blue_matrix = matrix[:, :, 0]

    if mapping_level == 0: # means high level 
        red_matrix = high_level_mapping_gray_scale(red_matrix, quantization_size)
        green_matrix = high_level_mapping_gray_scale(green_matrix, quantization_size)
        blue_matrix = high_level_mapping_gray_scale(blue_matrix, quantization_size)
    if mapping_level == 1: # means low level 
        red_matrix = low_level_mapping_gray_scale(red_matrix, quantization_size)
        green_matrix = low_level_mapping_gray_scale(green_matrix, quantization_size)
        blue_matrix = low_level_mapping_gray_scale(blue_matrix, quantization_size)
    if mapping_level == 2: # means middle level 
        red_matrix = mid_level_mapping_gray_scale(red_matrix, quantization_size)
        green_matrix = mid_level_mapping_gray_scale(green_matrix, quantization_size)
        blue_matrix = mid_level_mapping_gray_scale(blue_matrix, quantization_size)
    
    modified_image = np.stack((blue_matrix, green_matrix, red_matrix), axis=-1)

    return modified_image