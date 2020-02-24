# main.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/14
# Last modified : 2020/02/24

import constant as c
import github as g
import sqlConnect as sql

# FILES

# ["name of systems", number of files]
FILES = [
    ["testng", 1]
]

filters = [" security ", " threat ", " vulnerability "]

g.increaseSizeLimit()

category = "issues"

filterTableColumns = ["id INT AUTO_INCREMENT PRIMARY KEY", "file MEDIUMTEXT", "line MEDIUMTEXT", "link MEDIUMTEXT", "date MEDIUMTEXT", "security INT"]
mergeTableColumns = ["id INT AUTO_INCREMENT PRIMARY KEY", "issueKey VARCHAR(255)", "title MEDIUMTEXT", "link MEDIUMTEXT", "date MEDIUMTEXT", "labels MEDIUMTEXT", "html MEDIUMTEXT"]
columns = ['file', "line", "link", 'date', "security"]

for file in FILES:
    print("\n[FILES] \tProcessing " + file[0])
    
    g.merge([c.INPUT_FILES], [c.OUTPUT_FILES], file[0], category, file[1])
    outFile, writeBuffer = g.filterSort("merge_" + file[0] + "_" + category, columns, filters, mergeTableColumns)
    #sql.save(outFile, filterTableColumns, columns, writeBuffer)
