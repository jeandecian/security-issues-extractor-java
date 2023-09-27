import urllib.request

import search


def isValidUrl(url):
    # checks if the url is valid
    return search.contains(url, "http")


def getWebsiteHtml(url):
    # get the html code from url
    return urllib.request.urlopen(url).read().decode("utf-8")


def containsElements(url, elements):
    # checks if the url contains elements
    if not isValidUrl(url):
        return False

    html = getWebsiteHtml(url)
    return search.contains(html, elements)
