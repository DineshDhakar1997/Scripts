from PIL import Image
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract' 

def extract_text_from_image(image):
    # image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text



def extract_first_frame(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read the first frame.")
        return

    cap.release()
    return frame






