# csvManager.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/23
# Last modified : 2019/05/30

import os
import csv
import sys
import time

import config as conf

def getPath(components):
    # get the absolute path of a file
    path = os.path.join(os.getcwd(), *components)
    
    return path if (".csv" in path) else path + ".csv"

def increaseSizeLimit():
    # increase the size because an error pops up when one field is longer than his size
    csv.field_size_limit(sys.maxsize)

def read(file):
    # return fields and contents from file
    fields = []
    contents = []
    with open(file, conf.READ_FILE, encoding=conf.ENCODING) as readFile:
        reader = csv.reader(readFile, delimiter=conf.DELIMITER)
        fields = next(reader)
        
        for row in reader:
            contents.append(row)
    readFile.close()

    return fields, contents

def save(file, fields, contents):
    # save fields and contents in file
    with open(file, conf.WRITE_FILE, encoding=conf.ENCODING, newline="") as writeFile:
        writer = csv.writer(writeFile, delimiter=conf.DELIMITER)
        writer.writerow(fields)
        for row in contents:
            writer.writerow(row)

        print("[CSV] \tFinished saving " + file.split(os.path.sep)[-1] + " (" + str(len(contents)) + " entries)")
    
    writeFile.close()
