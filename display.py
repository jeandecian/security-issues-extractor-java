# display.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/27
# Last modified : 2019/05/29

def loading(load):
    print(load, end="")

def processing(file):
    print("Processing " + file)

def processingFile(file, number, total):
    print("Processing " + file + " (" + str(number) + "/" + str(total) + ")", end=" ")
