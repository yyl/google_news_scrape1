import urllib2
from xml.dom.minidom import parseString

def get_google_new_results( term, count ):
    results = []
    #obj = parseString( urllib2.urlopen('https://news.google.com/news?q=%s&output=rss' % term).read() )
    req = urllib2.Request('http://news.google.com/news?q=%s&output=rss' % term, headers={'User-Agent': 'Mozilla/5.0'})
    obj = parseString(urllib2.urlopen(req).read())
    elements = obj.getElementsByTagName('title')[2:] # To get rid of unwanted title elements in XML doc    
    links = obj.getElementsByTagName('link')[2:]
    print links
    for element in elements[:count]:
        headline =  element.childNodes[0].data
        for link in links:
            url = link.childNodes[0].data.split('=')[-1]
        newssearch = headline + ' -> ' + url
        results.append( newssearch )

    return results

items = get_google_new_results( 'apple', 2 )
for i,e in enumerate(items):
    print '%d: %s' % (i+1,e,)
