from video_ocr import extract_first_frame
from crop_function import crop_image
from video_ocr import  extract_text_from_image

from split_function import split_by_special_chars
import os
import cv2
import numpy as np
from PIL import Image
from word_validator import is_valid_word
import glob

all_video_paths = sorted(glob.glob('/Users/dinesh/Downloads/AlgoExpert/4 Very hard/*.mp4'))
for video_path in all_video_paths:
    first_frame=extract_first_frame(video_path)
    pil_image = Image.fromarray(cv2.cvtColor(first_frame, cv2.COLOR_BGR2RGB))
    left, top, right, bottom = 0,0, 1050, 100
    cropped_image=crop_image(first_frame, left, top, right, bottom)
    lesson=video_path.split('/')[-1].replace('.mp4','')
    cv2.imwrite(f'images/{lesson}.jpg', cv2.cvtColor(np.array(cropped_image), cv2.COLOR_RGB2BGR))
    extracted_text = extract_text_from_image(cropped_image)
    input_string = extracted_text
    result_list = split_by_special_chars(input_string)
    txt_list=result_list
    

    new_name=''




    for word in txt_list:
        if word.isalpha():
            new_name+=word+' '
        
    # print('new_name=>',new_name)
    if new_name=='':
        break
    else:
        splitted=video_path.split('/')
        splitted[-1]=new_name.strip()+'.mp4'
        new_path='/'.join(splitted)
        # print(video_path.split('/')[-1],splitted[-1])
        os.rename(video_path,new_path)





        

