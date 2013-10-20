#TV Release Module by o9r1sh September 2013

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,sys,main,xbmc,os
import urlresolver

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))

base_url = 'http://tv-release.net'

def TV_CATEGORIES():
        main.addDir('XVID Episodes',base_url + '/category/tvshows/tvxvid/',130,artwork + '/main/xvidtv.png')
        main.addDir('MP4 Episodes',base_url + '/category/tvshows/tvmp4/',130,artwork + '/main/mp4tv.png')
        main.addDir('480P Episodes',base_url + '/category/tvshows/tv480p',130,artwork + '/main/sdtv.png')
        main.addDir('720P Episodes',base_url + '/category/tvshows/tv720p/',130,artwork + '/main/hdtv.png')
        main.addDir('Foreign Episodes',base_url + '/category/tvshows/tv-foreign',130,artwork + '/main/foreign.png')
        main.addDir('Search',base_url + 'none',128,artwork + '/main/search.png')

def HDMOVIES():
        INDEX(base_url + '/category/movies/movies720p')

        
def MOVIE_CATEGORIES():
        main.addDir('XVID Movies',base_url + '/category/movies/moviesxvid',130,artwork + '/main/xvidmovies.png')
        main.addDir('480P Movies',base_url + '/category/movies/movies480p',130,artwork + '/main/sdmovies.png')
        main.addDir('720P Movies',base_url + '/category/movies/movies720p',130,artwork + '/main/hdmovies.png')
        main.addDir('DVD-R Movies',base_url + '/category/movies/moviesdvdr',130,artwork + '/main/dvdrmovies.png')
        main.addDir('Foreign Movies',base_url + '/category/movies/moviesforeign',130,artwork + '/main/foreign.png')
        
def INDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('a href="(.+?)"><b><font size=".+?">(.+?)</font></b></a>').findall(link)
        np=re.compile("<span class='zmg_pn_current'>(.+?)</span>").findall(link)
        np_url = None
        cur_page = None
        if len(np) > 0:
                cur_page = np[0]
                cur_page = int(cur_page)
                next_page = int(cur_page) + 1
                if cur_page == 1:
                        np_url = url + '/page/' + str(next_page)

                else:
                        head,sep,tail = url.partition('/page/')
                        np_url = head + sep + str(next_page)

                if '&cat' in url:
                                head,sep,tail = url.partition('?s')
                                np_url = base_url + '/page/' + str(next_page) +'/' + sep + tail

                
                        
                main.addDir('Next Page',np_url,130,artwork + '/main/next.png')

        for url,name in match:
                try:
                        if 'Filech' in name:
                                continue
                        else:
                                main.addDir(name,url,129,'')
                except:
                        continue

def VIDEOLINKS(name,url,thumb):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile("<a target='_blank' href='(.+?)'>").findall(link)
        for url in match:
                        hmf = urlresolver.HostedMediaFile(url)
                        if hmf:
                                host = hmf.get_host()
                                hthumb = main.GETHOSTTHUMB(host)
                                main.addHDir(name,url,9,thumb,hthumb)

def SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = search.replace(' ','%20')
                url = base_url + '/?s=' + search + '&cat='
                
                INDEX(url)
