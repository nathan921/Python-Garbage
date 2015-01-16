__author__ = 'e228596'
import urllib2
from bs4 import BeautifulSoup

redirs = []

JUMPS = 2
page = 'http://harrypotter.wikia.com/wiki/12_Grimmauld_Place'
f = open('dict.txt', 'w')

for i in range(0, JUMPS):
    if i == 1:
        page = 'http://harrypotter.wikia.com/wiki/Marauder%27s_Map'
    if i > 1:
        page = 'http://harrypotter.wikia.com/wiki/Special:Random'
    response = urllib2.urlopen(page)
    html = response.read()
    soup = BeautifulSoup(html)
    #main_content = soup.find('div', {'id' : 'mw-content-text'})
    title = soup.find('header', {'id':'WikiaPageHeader'}).find('h1').text
    print 'CONTENT:' + title
    f.write(title.replace(" ","").replace("'", "")+'\n')
    f.write(title.replace(" ","").replace("'", "").lower()+'\n')
    content = soup.find_all('p')

    for tag in content:
        aTags = tag.find_all('a')
        for oTag in aTags:
            if '[' not in oTag.text:
                if oTag.text not in redirs:
                    redirs.append(oTag['href'])
                    f.write(oTag.text.replace(" ", "").replace("'", "")+'\n')
                    f.write(oTag.text.replace(" ", "").replace("'", "").lower()+'\n')
                else:
                    print 'Duplicate Entry Skipped'

for j in range(0, len(redirs)):
    print 'Page ' + str(j) + ' of ' + str(len(redirs))
    if 'http' not in redirs[j]:
        page = 'http://harrypotter.wikia.com' + redirs[j]
    response = urllib2.urlopen(page)
    html = response.read()
    soup = BeautifulSoup(html)

    title = soup.find('header', {'id':'WikiaPageHeader'}).find('h1').text
    try:
        title.encode('ascii')
    except UnicodeEncodeError:
        print 'Ascii Error: Skipped'
    else:
        print 'CONTENT:' + title
        f.write(title.replace(" ","").replace("'", "")+'\n')
        f.write(title.replace(" ","").replace("'", "").lower()+'\n')



    content = soup.find_all('p')

    for tag in content:
        aTags = tag.find_all('a')
        for oTag in aTags:
            if '[' not in oTag.text:
                try:
                    oTag.text.encode('ascii')
                except UnicodeEncodeError:
                    print 'Ascii Error: Skipped'
                else:
                    f.write(oTag.text.replace(" ", "").replace("'", "")+'\n')
                    f.write(oTag.text.replace(" ", "").replace("'", "").lower()+'\n')

f.close()

lines_seen = set() # holds lines already seen
outfile = open('dict_no_dupes.txt', "w")
for line in open('dict.txt', "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()