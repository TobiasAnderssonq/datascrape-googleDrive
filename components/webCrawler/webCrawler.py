import requests    
import re
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

class PyCrawler(object):
    def __init__(self):     
        self.visited = set()
        #self.parent = parent    

    def get_html(self, url):    
        try:    
            html = requests.get(url)    
        except Exception as e:    
            print(e)    
            return ""    
        return html.content.decode('latin-1')    

    def get_links(self, url):    
        html = self.get_html(url)    
        parsed = urlparse(url)    
        base = parsed.scheme + "://" + parsed.netloc
        links = re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', html)    
        for i, link in enumerate(links):    
            if not urlparse(link).netloc:    
                link_with_base = base + link    
                links[i] = link_with_base       

        return set(filter(lambda x: 'mailto' not in x, links))    

    def extract_info(self, url):                                
        html = self.get_html(url)                               
        return None                  

    def crawl(self, url):                   
        for link in self.get_links(url):    
            if link in self.visited:        
                continue                                   
            self.visited.add(link)
            #self.parent.update_visited(link)            
            info = self.extract_info(link)   
            print(link) 
            self.crawl(link)                  

    def start(self, starting_url):                     
        self.crawl(starting_url)

if __name__ == '__main__':
    pycrawler = PyCrawler()
    pycrawler.start("https://en.wikipedia.org/wiki/Wikipedia:Random")