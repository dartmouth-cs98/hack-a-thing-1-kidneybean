# Followed tutorial from https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

# import libraries
import urllib2
from bs4 import BeautifulSoup

def main():
    NUM_PAGES = 10
    pages = []

    for i in range(0,NUM_PAGES):
        # specify the url
        url = "https://en.wikipedia.org/wiki/Special:Random"

        # query the website and return the html to the variable "page"
        page = urllib2.urlopen(url)

        # parse the html using beautiful soap and store in variable `soup`
        soup = BeautifulSoup(page, "html.parser")

        title = soup.title.text.strip()
        title = title[:-12]

        # Take out the <div> of name and get its value
        num_links = 0

        for link in soup.find_all('a'):
            #print(link.get('href'))
            num_links+=1

        tuple = (title, num_links)
        pages.append(tuple)
    sorted_pages = list(reversed(sorted(pages, key=getNumLinks)))

    average = 0
    for i in range(0,NUM_PAGES):
        print str(i+1) + ". \"" + sorted_pages[i][0] + "\" has " + str(sorted_pages[i][1]) + " links."
        average += sorted_pages[i][1]

    print "\nThe average number or links in this set of pages is " + str(average/NUM_PAGES)

def getNumLinks(item):
    return item[1]

main()

#name = name_box.text.strip() # strip() is used to remove starting and trailing

# get the index price
#price_box = soup.find("div", attrs={"class":"price"})
#price = price_box.text
#print price
