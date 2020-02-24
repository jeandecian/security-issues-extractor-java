# github.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/27
# Last modified : 2020/02/24

import csv
import time

import constant as c
import csvManager
import display as disp
import requests as req
import search
import sqlConnect as sql

def increaseSizeLimit():
    csvManager.increaseSizeLimit()

def merge(pathIn, pathOut, file, category, count):
    # merge all github files from same repo into one + add the html code
    processFile = file + "_" + category
    fields = []
    unique = []
    writeBuffer = []
    totalTime = 0

    for i in range(count):
        startTime = time.time()
        disp.processingFile(processFile, i + 1, count)
        path = pathIn.copy()
        path.append(processFile + "_" + str(i + 1) + ".csv")
        fields, contents = csvManager.read(csvManager.getPath(path))
            
        for row in contents:
            disp.loading(".")
            if ((row[fields.index("id")] not in unique) and (len(row) == len(fields))):
                unique.append(row[fields.index("id")])
                row.append(req.getWebsiteHtml(row[fields.index("link")]))
                writeBuffer.append(row)

        diffTime = round(time.time() - startTime, 2)
        print(" " + str(diffTime))
        totalTime += diffTime

    print("\n[GIT] \tProcessing " + processFile + " took in total " + str(round(totalTime, 2)) + "s (" + str(len(writeBuffer)) + ")")
    pathOut.append("merge_" + processFile)
    fields.append("html")
    csvManager.save(csvManager.getPath(pathOut), fields, writeBuffer)

def filterSort(file, columns, filters, mergeTableColumns):
    # filter the merge github file and sort
    fields, contents = csvManager.read(csvManager.getPath([c.OUTPUT_FILES, file]))
    fields[fields.index("id")] = "issueKey"
    writeBuffer = []
    outFile = file.replace(".", "")
    outFile = outFile.replace("-", "")
    # sql.save(outFile, mergeTableColumns, fields, contents)
    
    for row in contents:
        html = row[fields.index("html")]

        # check if html contains some key word related to security
        security = "1" if search.contains(html, filters) and search.contains(html, "bug") else 0

        # retrive every files that match .java file
        # add ":" after because sometimes, it has the line after
        files = search.handleExtraction(html, "()", ".java:")
        
        if (files):
            date = search.extractElement("relative-time", html, "/relative-time")
            date = search.extractElement("\"", date, "T")
                
            for f in files:
                rowBuffer = []
                fl = f.split(":")
                rowBuffer.append(fl[0])
                rowBuffer.append(fl[-1])
                rowBuffer.append(row[fields.index("link")])
                rowBuffer.append(date)
                rowBuffer.append(security)
                    
                writeBuffer.append(rowBuffer)

    outFile = outFile.replace("merge_", "out_")
    pathOut = [c.OUTPUT_FILES, outFile]
    csvManager.save(csvManager.getPath(pathOut), columns, writeBuffer)

    return outFile, writeBuffer
