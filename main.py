# main.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/14
# Last modified : 2019/06/26

import github as g
import issueTrackingSystem as its
import sqlConnect as sql

# FILES

# Si cela provient d'un Issue Tracking System, sinon enlever
ITS_FILES = ["infinispan", "jenkins", "wildfly"]

# Si cela provient de GitHub
# Sous la forme ["nom du repertoire", [nombre de fichiers issues, nombre de fichiers pull request]]
G_FILES = [
    ["glassfish", [106, 0]],
    ["elasticsearch", [63, 16]],
    ["spring-security", [28, 0]],
    ["orientdb", [8, 0]],
    ["jetty.project", [8, 0]],
    ["neo4j", [5, 0]],
    ["hazelcast", [4, 2]],
    ["presto", [3, 0]],
    ["exist", [3, 1]]
]

filters = [" security ", " threat ", " vulnerability "]

# ISSUE TRACKING SYSTEM - enlever si pas necessaire

its.increaseSizeLimit()

fileType = ".java"
    
filterFields = ['Issue key', 'Created', 'Priority', 'Summary', 'Description']
    
filterTableColumns = ["id INT AUTO_INCREMENT PRIMARY KEY", "issueKey VARCHAR(255)", "created VARCHAR(255)", "priority VARCHAR(255)", "summary MEDIUMTEXT", "description MEDIUMTEXT", "security INT"]
filterColumns = ['issueKey', 'created', 'priority', 'summary', 'description', 'security']

sortFields = ["File", "Line", "Issue key", "Date", "Priority", "Security"]

sortTableColumns = ["id INT AUTO_INCREMENT PRIMARY KEY", "file VARCHAR(255)", "line VARCHAR(255)", "link MEDIUMTEXT", "date VARCHAR(255)", "priority VARCHAR(255)", "security INT"]
sortColumns = ['file', 'line', 'link', 'date', 'priority', "security"]

for file in ITS_FILES:
    print("\n[ITS] \tProcessing " + file)
    pathIn = ["its_export"]
    pathOut = ["its_out"]

    outFile, writeBuffer = its.filter(pathIn, pathOut, file, filterFields, fileType, filters)
    sql.save(outFile, filterTableColumns, filterColumns, writeBuffer)

    pathIn = ["its_out"]
    pathOut = ["its_out"]

    outFile, writeBuffer = its.sort(pathIn, pathOut, file, sortFields)
    sql.save(outFile, sortTableColumns, sortColumns, writeBuffer)

# GITHUB - enlever si pas necessaire

g.increaseSizeLimit()

categories = ["issues", "pulls"]

filterTableColumns = ["id INT AUTO_INCREMENT PRIMARY KEY", "file MEDIUMTEXT", "line MEDIUMTEXT", "link MEDIUMTEXT", "date MEDIUMTEXT", "security INT"]
mergeTableColumns = ["id INT AUTO_INCREMENT PRIMARY KEY", "issueKey VARCHAR(255)", "title MEDIUMTEXT", "link MEDIUMTEXT", "date MEDIUMTEXT", "labels MEDIUMTEXT", "html MEDIUMTEXT"]
columns = ['file', "line", "link", 'date', "security"]

for gFile in G_FILES:
    file = gFile[0]
    count = gFile[1]
    print("\n[GIT] \tProcessing " + file)

    pathIn = ["github_export"]
    pathOut = ["github_merge"]
    
    for index, category in enumerate(categories):
        if (count[index]):
            g.merge(pathIn, pathOut, file, category, count[index])
            outFile, writeBuffer = g.filterSort("merge_" + file + "_" + category, columns, filters, mergeTableColumns)
            sql.save(outFile, filterTableColumns, columns, writeBuffer)
