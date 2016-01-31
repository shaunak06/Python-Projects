import urllib
import re


def forecast_for_zip(zipcode):
    #<meta name="og:title" content="Orange, CT | 71.1&deg; | Mostly Cloudy" />
    
    w_url = "http://www.wunderground.com/cgi-bin/findweather/hdfForecast"
    params = urllib.urlencode({'query' : zipcode})
    f = urllib.urlopen(w_url, params )
    webpage = f.read()

    forecastpat= 'meta name="og:title" content="(.*), (.*)\| (.*)&deg; \| (.*)'

    forecast_re = re.compile(forecastpat, re.MULTILINE)
    m = forecast_re.search(webpage)
    
    if m:
         retmap = {"city" : m.group(1), "state" : m.group(2), "temp" : m.group(3), "quality": m.group(4)}
         return retmap
    else:
         return None
    
if __name__ == "__main__":

    print(forecast_for_zip("06460")) #insert zip code
 
