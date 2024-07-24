import os
import shutil
import sys

src = r'E:\Desktop 2\Desktop\New Work Vijaykarthick\App_Indore City FMCG Retailers\\'
dest = r'E:\Desktop 2\Desktop\Full Image\\'
src_files = os.listdir(src)
for folder in src_files:    
    ls = os.listdir(src+folder)
    for l in ls:
        #print (l)
        img_path = src+folder+'\\'+l
        print(img_path)
        shutil.copy(img_path, dest)

