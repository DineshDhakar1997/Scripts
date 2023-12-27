import glob
import os
import numpy as np
import shutil
num=[str(i).zfill(3) for i in np.arange(1000)]
with open('series.txt','r') as f:
    lines=f.readlines()
new_cont=''
for line in lines:
    if len(line)==7 and 'm ' in line and 's' in line:
        continue
    else:
        new_cont=new_cont+line

i=1
new_cont=new_cont.split('\n')
files=glob.glob('/Users/dinesh/Downloads/react18-copy/*.mp4')
files.sort()
i=0
for f in files:
    dp=f'/Users/dinesh/Downloads/react18-copy/{str(int(i/15))}'
    if not os.path.exists(dp):
        os.mkdir(dp)
    new_path=dp+'/'+f.split('/')[-1]
    print(new_path)
    shutil.copy(f,new_path)
    i+=1
    

    
    
    
        
        
        


    

# for  folder in folders:
    
#     print(folder.split('/')[-1])
#     for video in glob.glob(folder+'/*'):
#         j=+1
#         split_vid=video.split('/')
        
#         for i in range(len(new_cont)):
                
#             if (new_cont[i]+'.mp4').replace(" ","") == video.split('/')[-1].replace(" ","") and new_cont[i]!='':
#                 last=video.split('/')[-1]
#                 new_file_name=f'{i}- '+last
#                 split_vid[-1]=new_file_name
#                 new_path='/'.join(split_vid)
#                 try:

#                     os.rename(video,new_path)
#                 except:
#                     pass
#                 print(video,'>>',new_path,'\n')
    

                

# for  folder in needed_folder:
#     i=0
#     print(folder.split('/')[-1])
#     folder_vid=sorted(glob.glob(folder+'/*'))
#     for video in glob.glob(folder+'/*'):
#         i+=1
#         # print(video)
#         formatted_number = "{:02d}.".format(i)
#         text_representation = str(formatted_number)
#         print(text_representation)
#         name=video.split('/')[-1]
#         # print(name)
#         newname= text_representation+name.split('. ')[-1]
#         print(newname)
#         split_vid=video.split('/')
#         split_vid[-1]=newname
        
        # print(split_vid)
        # new_path='/'.join(split_vid)
        # print(new_path)
        # os.rename(video,new_path)



                









    




