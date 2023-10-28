import urllib3
from bs4 import BeautifulSoup

course_code = "9.14"
course_replaced = course_code.replace(".", "-")

page = urllib3.request("GET", "https://ocw.mit.edu/sitemap.xml")

def getLocs(data):
    pageSoup = BeautifulSoup(data, 'xml')
    locs = pageSoup.findAll("loc")
    return list(map(lambda x: x.contents[0], locs))

def getCourseSitemap(sitemaps):
    for sitemap in sitemaps:
        if course_replaced in sitemap:
            return sitemap
    
locContents = getLocs(page.data)
courseSitemap = getCourseSitemap(locContents)

page = urllib3.request("GET", courseSitemap)

courseContents = getLocs(page.data)
for content in courseContents:
    if "resources/assignments" in content:
        print("Assignments Resources: " + content)