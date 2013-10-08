#NewMyVideoLinks Module by o9r1sh September 2013

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,sys,main,xbmc,os
import urlresolver

addon_id = 'plugin.video.videophile'
from t0mm0.common.addon import Addon
addon = Addon(addon_id, sys.argv)

mode = addon.queries['mode']
url = addon.queries.get('url', '')
name = addon.queries.get('name', '')
thumb = addon.queries.get('thumb', '')
year = addon.queries.get('year', '')
types = addon.queries.get('types', '')

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))

base_url = 'http://www.myvideolinks.eu'

def CATEGORIES():
        main.addDir('Yify Movies',base_url + '/category/movies/yify/',18,artwork + 'yify.png')
        main.addDir('Recent Movies',base_url + '/category/movies/',18,artwork + 'recentlyadded.png')
        main.addDir('Search','none',21,artwork + 'search.png')

def TVCATEGORIES():
        main.addDir('Recent Episodes',base_url + '/category/tv-shows/',18,artwork + 'recentlyadded.png')
        main.addDir('Search','none',21,artwork + 'search.png')
        
def INDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)" rel=".+?" title=".+?"> <img src="(.+?)" width=".+?" height=".+?" title="(.+?)" class=".+?"></a>').findall(link)
        np=re.compile("<span class='pages'>Page (.+?)</span>").findall(link)
        if len(np) > 0:
                numbers = np[0]
                head,sep,tail = numbers.partition('of')
                current_page = int(head)
                last_page = int(tail)
                nex = current_page + 1
                if nex < last_page:
                        if current_page == 1:
                                next_page = url + '/page/' + str(nex)
                        else:
                                a,b,c = url.partition('/page/')
                                next_page = url + a + b + str(nex)
                        main.addDir('Next Page',next_page,18,artwork + 'next.png')

        for url,thumbnail,name in match:
                if len(match) > 0:
                        try:        
                                main.addMDir(name,url,19,thumbnail,'')
                        except:
                                continue

def VIDEOLINKS(name,url,thumb,year):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<li><a href="(.+?)">.+?</a></li>').findall(link)
        for url in match:
                if len(match) > 0:
                                hmf = urlresolver.HostedMediaFile(url)
                                if hmf:
                                        host = hmf.get_host()
                                        print 'tttttttttt' + host
                                        hthumb = main.GETHOSTTHUMB(host)
                                        main.addHDir(name,url,9,thumb,hthumb)

def SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = search.replace(' ','+')
                
                url = base_url + '/index.php?s=' + search
                print url
                
                INDEX(url)
