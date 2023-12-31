# -*- coding: utf-8 -*-
"""create_batch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T2wsQSryS71LBIv0iArIsu7GsuV73vAe
"""

import os
import shutil
folder_loc="/Users/dineshdhakar/Desktop/9"
all_path_to_batches = [os.path.join(folder_loc, filename) for filename in os.listdir(folder_loc)]
print(all_path_to_batches)
for path in all_path_to_batches:
    file_ext=path.split(".")
    if file_ext[-1]=="DS_Store":
        os.remove(path)
        all_path_to_batches.remove(path)

for i in range(len(all_path_to_batches)):
    print(all_path_to_batches[i])
    shutil.make_archive(all_path_to_batches[i]+".zip", folder_loc)
    shutil.rmtree(all_path_to_batches[i])