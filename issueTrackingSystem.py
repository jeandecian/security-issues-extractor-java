# issueTrackingSystem.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/27
# Last modified : 2019/05/31

import csvManager
import search

def increaseSizeLimit():
    csvManager.increaseSizeLimit()

def filter(pathIn, pathOut, file, filterFields, fileType, securityFilters):
    # filter the file through filterFields, fileType
    # returns outFile and writeBuffer
    writeBuffer = []
    path = pathIn.copy()
    path.append(file)
    fields, contents = csvManager.read(csvManager.getPath(path))
        
    for row in contents:
        if (search.contains(row, fileType)):
            rowBuffer = []
            indexBuffer = []
            for field in filterFields:
                fieldIndex = fields.index(field)
                if (fieldIndex in indexBuffer):
                    fieldIndex += 1
                indexBuffer.append(fieldIndex)

                if (field != "Description"):
                    rowBuffer.append(row[fieldIndex])
                else:
                    rowBuffer.append("\n".join(search.handleExtraction(row[fieldIndex], "()", fileType)))

            security = "1" if search.contains(row, securityFilters) and search.contains(row, "bug") else 0
            rowBuffer.append(security)
            writeBuffer.append(rowBuffer)

    outFile = "filtered_" + file
    path = pathOut.copy()
    path.append(outFile)
    saveFields = filterFields.copy()
    saveFields.append("Security")

    csvManager.save(csvManager.getPath(path), saveFields, writeBuffer)

    return outFile, writeBuffer

def sort(pathIn, pathOut, file, sortFields):
    # sort the file through sortFields
    # returns outFile and writeBuffer
    writeBuffer = []
    path = pathIn.copy()
    path.append("filtered_" + file)
    fields, contents = csvManager.read(csvManager.getPath(path))

    for row in contents:
        extractFiles = search.getFiles(row[fields.index("Description")].split("\n"))        
        link = "https://issues.jenkins-ci.org/browse/" if "jenkins" in file else "https://issues.jboss.org/browse/"
        
        for extract in extractFiles:
            rowBuffer = []
            rowBuffer.append(extract[0])
            rowBuffer.append(extract[len(extract)-1])
            rowBuffer.append(link + row[fields.index("Issue key")])
            rowBuffer.append(row[fields.index("Created")].split(" ")[0])
            rowBuffer.append(row[fields.index("Priority")])
            rowBuffer.append(row[fields.index("Security")])
            writeBuffer.append(rowBuffer)

    outFile = "sort_" + file
    path = pathOut.copy()
    path.append(outFile)

    csvManager.save(csvManager.getPath(path), sortFields, writeBuffer)

    return outFile, writeBuffer
