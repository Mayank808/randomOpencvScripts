import os
import shutil
import random

def merge_samples(end_dir):
    index = 0
    for data_set in range(0, 5):
        bounding_box = {}
        file_path = f'allSamples/info{data_set}/info{data_set}.lst'
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                parts = line.split(' ', 1)
                bounding_box[parts[0]] = parts[1]
        print(f'{len(bounding_box)} total number of sample images')

        dir_name = f'allSamples/info{data_set}'
        with open('newInfo.lst', 'a') as f: 
            all_files = os.listdir(dir_name)
            random_files = random.sample(all_files, 1250)
            for file in random_files:
                if file == f"info{data_set}.lst":
                    continue
                old_file_path = f"{dir_name}/{file}"
                write_in_info_file_name = f"{index}{os.path.splitext(file)[1]}"
                new_file_path = f"{end_dir}/{write_in_info_file_name}"
                f.write(f"{write_in_info_file_name} {bounding_box[file]}\n")
                shutil.copy2(old_file_path, new_file_path)
                index += 1
        print(f"Completed info{data_set}")        
    print(f"Completed All should have compiled a total of {index} images")

merge_samples('compiled')
