# crop_function.py
import cv2
from PIL import Image

def crop_image(input_image, left, top, right, bottom):
    new_image=Image.fromarray(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))

    cropped_image = new_image.crop((left, top, right, bottom))
    # cropped_image=Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
    return cropped_image


