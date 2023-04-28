import cv2
import numpy as np
import os
import shutil

def create_neg_bgtxt():
    for file_type in ['neg']:
        for image in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type + '/' + image + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)
    print("Completed")
      
def resizeImagesInDirectory(start_dir, end_dir, width = 150):
    min_height, max_height = float("inf"), 0
    for file_name in os.listdir(start_dir):
        image_path = f"{start_dir}/{file_name}"
        print(image_path)
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        width_ratio = img.shape[1] / width 
        height = int(img.shape[0] / width_ratio) 
        
        min_height = min(min_height, height)
        max_height = max(max_height, height)
        
        resized_image = cv2.resize(img, (width, height), interpolation = cv2.INTER_LINEAR)
        cv2.imwrite(f'{end_dir}/{file_name}', resized_image)
    
    print(f"Completed: Max Height = {max_height}, Min Height = {min_height}, Constant Width = {width}")



def resize_Positives(start_dir, end_dir, height = 50):
    max_width = 0
    min_width = float('inf')
    for file_name in os.listdir(start_dir):
        image_path = f"{start_dir}/{file_name}"
        print(image_path)
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        height_ratio = img.shape[0] / height 
        width = int(img.shape[1] / height_ratio) 
        max_width = max(width, max_width)
        min_width = min(width, min_width)
        resized_image = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
        name = file_name.split('.')[0]
        cv2.imwrite(f'{end_dir}/{name}.png', resized_image)
    print(f"Completed: Max Height = {height}, Max Width = {max_width}, Min Width = {min_width}")


def rename_In_Directory(start_dir, end_dir, name):
    index = 0
    for file_name in os.listdir(start_dir):
        if file_name == '.DS_Store': 
            continue
        image_path = f'{start_dir}/{file_name}'
        ext = os.path.splitext(file_name)[1]
        new_path = f'{end_dir}/{name}{index}{ext}'
        shutil.copy2(image_path, new_path)
        index += 1
    print("Done")
    
def grayscale(start_dir, end_dir):
    for file_name in os.listdir(start_dir):
        image_path = f"{start_dir}/{file_name}"
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'{end_dir}/{file_name}', img)
        print(image_path)
        
def create_BG_txt(dir, file):
    with open(file, 'a') as f:
        for file_name in os.listdir(dir):
            f.write(f'neg/{file_name}\n') 
        
def main():
    # grayscale("otherUniCardNeg", "otherUniCardNeg")
    create_BG_txt("otherUniCardNeg", "otherCardNeg.txt")
    print("Completed")
    
if __name__ == "__main__":
    main()
    