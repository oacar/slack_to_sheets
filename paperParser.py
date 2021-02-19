from bs4 import BeautifulSoup
import urllib.request as urllib2
from urllib.error import HTTPError
import re

def get_paper_title(text):
    splt = text.split('https://')
    link = f"https://{splt[-1][:-1]}"
    #print(link)
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    try:
        req = urllib2.Request(link, headers=hdr)
        r = urllib2.urlopen(req)
        soup = BeautifulSoup(r,features="html.parser")
#        doi = soup.find_all("doi")
#        columns = soup.findAll('span', text = re.compile('doi'))
        return soup.title, link
    except HTTPError:
        print('Link is broken')
        pass

if __name__=='__main__':
    text = 'https://www.biorxiv.org/content/10.1101/2021.02.17.430503v1?'

    get_paper_title(text)