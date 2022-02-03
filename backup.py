import os
import shutil

source = input("Enter source folder name:")
destination = input("Enter destination folder name:")

source = source + "/"
destination = destination + "/"

lof = os.listdir(source)

for files in lof:
    shutil.copy((source+files),destination)