# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 17:16:54 2020

@author: nikhi
"""


import os

#Get the current working directory
cur_path = os.getcwd() + "\\"
#Get the files in the workingdirectory\files
files_indir = os.listdir('files')
#Get the paths of the files
paths = [f'files\{x}' for x in files_indir]
#Get the complete paths of the files
absolute_paths = []
for path in paths:
    temp= cur_path+ path 
    absolute_paths.append(temp)
    
#Get the contents of the file which has the oldest creation time
first_file = min(absolute_paths,key = os.path.getctime)

with open(os.path.abspath(first_file),'r') as f:
    print(f.read())
    
    