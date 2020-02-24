# main.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/14
# Last modified : 2020/02/24

import github as g
import sqlConnect as sql

# FILES

# Sous la forme ["nom du repertoire", [nombre de fichiers issues]]
G_FILES = [
    ["testng", [1, 0]]
]

filters = [" security ", " threat ", " vulnerability "]

g.increaseSizeLimit()

categories = ["issues"]

filterTableColumns = ["id INT AUTO_INCREMENT PRIMARY KEY", "file MEDIUMTEXT", "line MEDIUMTEXT", "link MEDIUMTEXT", "date MEDIUMTEXT", "security INT"]
mergeTableColumns = ["id INT AUTO_INCREMENT PRIMARY KEY", "issueKey VARCHAR(255)", "title MEDIUMTEXT", "link MEDIUMTEXT", "date MEDIUMTEXT", "labels MEDIUMTEXT", "html MEDIUMTEXT"]
columns = ['file', "line", "link", 'date', "security"]

for gFile in G_FILES:
    file = gFile[0]
    count = gFile[1]
    print("\n[FILES] \tProcessing " + file)

    pathIn = ["github_export"]
    pathOut = ["github_merge"]
    
    for index, category in enumerate(categories):
        if (count[index]):
            g.merge(pathIn, pathOut, file, category, count[index])
            outFile, writeBuffer = g.filterSort("merge_" + file + "_" + category, columns, filters, mergeTableColumns)
            #sql.save(outFile, filterTableColumns, columns, writeBuffer)
