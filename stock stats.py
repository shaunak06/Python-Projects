import urllib
import re


def stats_for_symbol(symbol):
    #<div class="hd"><div class="title"><h2>Google Inc. (GOOG)</h2>
    #<span class="time_rtq_ticker"><span id="yfs_l84_goog">886.38</span>
    #52wk Range:</th><td class="yfnc_tabledata1"><span>623.41</span> - <span>928.00</span>
    w_url = "http://finance.yahoo.com/q"
    params = urllib.urlencode({'s' : symbol})
    f = urllib.urlopen(w_url, params )
    webpage = f.read()
    #print webpage
    #return
   
   
    companypat = '\<div class="title"\>\s*\<h2\>(.*)\</h2\>'
    pricepat= '\<span class="time_rtq_ticker"\>\<span id="[\w\d_]*"\>([\d\.]*)\</span\>'
    rangepat = '52wk Range:\</th\>\<td class="yfnc_tabledata1"\>\<span\>([\d\.]*)\</span\> - \<span\>([\d\.]*)\</span\>'
    
    symbol_re = re.compile(companypat, re.MULTILINE)
    m = symbol_re.search(webpage)
    if m:
        print m.group(1)
    else:
        print "patern {0} did not match".format(companypat)
        
    symbol_re = re.compile(pricepat, re.MULTILINE)
    r = symbol_re.search(webpage)
    if r:
        print r.group(1)
    else:
        print "patern {0} did not match".format(pricepat)
        
    symbol_re = re.compile(rangepat, re.MULTILINE)
    p = symbol_re.search(webpage)
    if p:
        print p.group(1),p.group(2)
    else:
        print "patern {0} did not match".format(rangepat)
    
    low=float(r.group(1))
    high=float(p.group(1))
    current=float(p.group(2))
    
    line=['.']
    line*10
    
    
    
    
    if m:
        retmap = {"company" : m.group(1)}
    else:
         return None
         
    if r:
        retmap.update({"current price" : r.group(1)})
    else:
        return None
        
    if r:
       retmap.update({"52 week low" : p.group(1), "52 week high": p.group(2)})
       return retmap
    else:
        return None



         
if __name__ == "__main__":

    print(stats_for_symbol("GOOG")) #insert symbol