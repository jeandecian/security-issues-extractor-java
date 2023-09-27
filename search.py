import constant as cons


def contains(multi, elements):
    # checks if one of multi contains one of elements
    if type(multi) == type(str()):
        multi = [multi]
    if type(elements) == type(str()):
        elements = [elements]

    for one in multi:
        for element in elements:
            if one.find(element) != cons.NOT_FOUND:
                return True

    return False


def multiHasDifferentForms(multi, element):
    # checks if multi has different forms of element
    return contains(multi, element) or contains(multi, element.capitalize())


def extractElement(left, element, right):
    # extract the element between left and right
    if left in element and right in element:
        return element[slice(element.index(left) + len(left), element.index(right))]

    return ""


def extractFile(text, delimiter, fileType):
    # extract specific file from a string
    left = delimiter[0]
    right = delimiter[1]
    file = extractElement(left, text, right)
    if len(file) and contains(file, fileType):
        return file

    return ""


def handleExtraction(paragraph, delimiter, fileType):
    # extract all specific files from a paragraph
    extraction = []
    for text in paragraph.split("\n"):
        file = extractFile(text, delimiter, fileType)
        if file != "":
            extraction.append(file)

    return extraction


def getFiles(extraction):
    # return the files and the line
    files = []
    for e in extraction:
        if len(e):
            files.append(e.split(":"))

    return files
