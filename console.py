import cv2
import numpy as np
from Utils import high_level_mapping_gray_scale, \
                low_level_mapping_gray_scale, \
                    mid_level_mapping_gray_scale, \
                        mapping_rgb


IMAGE_URL = './images/blue_dice.png'


print("""
        Welcome to Computer Vision: A Gray Scale Quantization.

        Enter the Quantization Size. Choose From (2, 4, 8, 16, 32, 64, 128)
    """)
user_input = input("Enter Input: ")
try:

    if type(int(user_input)) != int:
        raise ValueError
    elif int(user_input) != 2 \
            and int(user_input) != 4 \
            and int(user_input) != 8 \
            and int(user_input) != 16 \
            and int(user_input) != 32 \
            and int(user_input) != 64 \
            and int(user_input) != 128:
        raise ValueError
    else:
        mappingLevel = input("""What kind of mapping do you want? 
            Press 0: High Level
            Press 1: Low Level
            Press 2: Middle Level
            : """)
        try:
            
            if int(mappingLevel) != 0 and int(mappingLevel) != 1 and int(mappingLevel) != 2:
                raise ValueError
            
            # Read the image in grayscale
            input_image_grayscale = cv2.imread(IMAGE_URL, 0) 
            # Read the image in RGB
            input_image_RGB = cv2.imread(IMAGE_URL)
            print("Processing Grey Level...")
            if int(mappingLevel) == 0:
                
                # Perform high level mapping on gray scale
                mappedImage = high_level_mapping_gray_scale(input_image_grayscale, int(user_input))
                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)

                # Display the original and mappedImage images
                cv2.imshow('Original Image GrayScale', input_image_grayscale)
                cv2.imshow(f'High Level {int(user_input)} Quantized Image GrayScale', mappedImage)
            elif int(mappingLevel) == 1:
                # Perform zero-order interpolation for image enlargement
                mappedImage = low_level_mapping_gray_scale(input_image_grayscale, int(user_input))
                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)

                # Display the original and mappedImage images
                cv2.imshow('Original Image GrayScale', input_image_grayscale)
                cv2.imshow(f'Low Level {int(user_input)} Quantized Image GrayScale', mappedImage)
            elif int(mappingLevel) == 2:
                # Perform zero-order interpolation for image enlargement
                mappedImage = mid_level_mapping_gray_scale(input_image_grayscale, int(user_input))
                mappedImage = np.array(mappedImage) 
                mappedImage = np.uint8(mappedImage)

                # Display the original and mappedImage images
                cv2.imshow('Original Image GrayScale', input_image_grayscale)
                cv2.imshow(f'Mid Level {int(user_input)} Quantized Image GrayScale', mappedImage)
            print("Grey Level Processing done.")
            print("Processing RGB Level...")
            if int(mappingLevel) == 0 or int(mappingLevel) == 1 or int(mappingLevel) == 2:
                # perform high level mapping on rgb
                mappedImage = mapping_rgb(input_image_RGB, int(user_input), int(mappingLevel))
                mappedImage = np.array(mappedImage)  # Your image data here
                mappedImage = np.uint8(mappedImage)

                # Display the original and enlarged images
                cv2.imshow('Original Image RGB', input_image_RGB)
                cv2.imshow(f'RGB {int(user_input)} Quantized Image RGB', mappedImage)
            print("RGB Processing done.")
            print("Waiting for all windows to Close")
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except ValueError as ev:
            print("Invalid input value: ")
            print(ev)

    
except ValueError as e:
    print("Invalid input: ")
    print(e)


# gray scale enlargment (single channel)



# # first order hold

# # Perform zero-order interpolation for image enlargement
# enlarged_image = first_order_enlargement_gray_scale(input_image_grayscale, FIRST_ORDER_KERNEL)

# enlarged_image = np.array(enlarged_image)  # Your image data here
# enlarged_image = np.uint8(enlarged_image)

# # Display the original and enlarged images
# cv2.imshow('Enlarged first order Image GrayScale', enlarged_image)



# cv2.waitKey(0)
# cv2.destroyAllWindows()