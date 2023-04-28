import cv2
import numpy as np
import os

mcgill_card_cascade = cv2.CascadeClassifier('models/model7/cascade.xml')
width = 150

def cleanDir(folder):
        for file in os.listdir(folder):
                if file[:6] == "marked" or file == ".DS_Store":
                        os.remove(f'{folder}/{file}')

def testDirectory(folder):
        cleanDir(folder)
        for file in os.listdir(folder):
                file_path = f'{folder}/{file}'
                print(file_path)
                img = cv2.imread(file_path, cv2.IMREAD_COLOR)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                width_ratio = img.shape[1] / width 
                height = int(img.shape[0] / width_ratio) 
                resized_image = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
                watches = mcgill_card_cascade.detectMultiScale(resized_image)

                for (x,y,w,h) in watches:
                        cv2.rectangle(resized_image,(x,y),(x+w,y+h),(240,248,255),2)
                
                cv2.imwrite(f'{folder}/marked{file}',resized_image)
                print(f"The photo {file} has {len(watches)} detections")

def testFile(file_path, width = 100):
        img = cv2.imread(file_path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print(img.shape)
        img = img[600:1220, 75:1000]
        cv2.imwrite(f'croppedImg.jpg', img)
        print(img.shape)
        width_ratio = img.shape[1] / width 
        height = int(img.shape[0] / width_ratio)

        print("THE DIMENSIONS ARE", img.shape)
        print("THE DIMENSIONS ARE", width, height) 
        resized_image = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
        watches = mcgill_card_cascade.detectMultiScale(resized_image)

        for (x,y,w,h) in watches:
                cv2.rectangle(resized_image,(x,y),(x+w,y+h),(240,248,255),2)
        
        cv2.imwrite(f'markedImage.jpg', resized_image)
        print(f"The photo {file_path} has {len(watches)} detections")

testDirectory('train')
print('done')
