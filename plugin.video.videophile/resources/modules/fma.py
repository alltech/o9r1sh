#FreeMoviesAddict Module by o9r1sh September 2013

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

settings = xbmcaddon.Addon(id='<plugin.video.videophile>')
artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://www.freemoviesaddict.com'

def CATEGORIES():
        main.addDir('Recent Movies',base_url,26,artwork + 'recentlyadded.png')
        main.addDir('A-Z','none',30,artwork + 'a-z.png')
        main.addDir('Genres','none',28,artwork + 'genres.png')
        main.addDir('Years','none',29,artwork + 'years.png')

def LETTERS():
        main.addDir('#',base_url + '/movies/letter/123',26,artwork + '#.png')
        main.addDir('A',base_url + '/movies/letter/A',26,artwork + 'a.png')
        main.addDir('B',base_url + '/movies/letter/B',26,artwork + 'b.png')
        main.addDir('C',base_url + '/movies/letter/C',26,artwork + 'c.png')
        main.addDir('D',base_url + '/movies/letter/D',26,artwork + 'd.png')
        main.addDir('E',base_url + '/movies/letter/E',26,artwork + 'e.png')
        main.addDir('F',base_url + '/movies/letter/F',26,artwork + 'f.png')
        main.addDir('G',base_url + '/movies/letter/G',26,artwork + 'g.png')
        main.addDir('H',base_url + '/movies/letter/H',26,artwork + 'h.png')
        main.addDir('I',base_url + '/movies/letter/I',26,artwork + 'i.png')
        main.addDir('J',base_url + '/movies/letter/J',26,artwork + 'j.png')
        main.addDir('K',base_url + '/movies/letter/K',26,artwork + 'k.png')
        main.addDir('L',base_url + '/movies/letter/L',26,artwork + 'l.png')
        main.addDir('M',base_url + '/movies/letter/M',26,artwork + 'm.png')
        main.addDir('N',base_url + '/movies/letter/N',26,artwork + 'n.png')
        main.addDir('O',base_url + '/movies/letter/O',26,artwork + 'o.png')
        main.addDir('P',base_url + '/movies/letter/P',26,artwork + 'p.png')
        main.addDir('Q',base_url + '/movies/letter/Q',26,artwork + 'q.png')
        main.addDir('R',base_url + '/movies/letter/R',26,artwork + 'r.png')
        main.addDir('S',base_url + '/movies/letter/S',26,artwork + 's.png')
        main.addDir('T',base_url + '/movies/letter/T',26,artwork + 't.png')
        main.addDir('U',base_url + '/movies/letter/U',26,artwork + 'u.png')
        main.addDir('V',base_url + '/movies/letter/V',26,artwork + 'v.png')
        main.addDir('W',base_url + '/movies/letter/W',26,artwork + 'w.png')
        main.addDir('X',base_url + '/movies/letter/X',26,artwork + 'x.png')
        main.addDir('Y',base_url + '/movies/letter/Y',26,artwork + 'y.png')
        main.addDir('Z',base_url + '/movies/letter/Z',26,artwork + 'z.png')

def GENRES():
        main.addDir('Action',base_url + '/movies/genre/action',26,artwork + 'action.png')
        main.addDir('Adventure',base_url + '/movies/genre/adventure',26,artwork + 'adventure.png')
        main.addDir('Animation',base_url + '/movies/genre/animation',26,artwork + 'animation.png')
        main.addDir('Biography',base_url + '/movies/genre/biography',26,artwork + 'biography.png')
        main.addDir('Comedy',base_url + '/movies/genre/comedy',26,artwork + 'comedy.png')
        main.addDir('Crime',base_url + '/movies/genre/crime',26,artwork + 'crime.png')
        main.addDir('Documentary',base_url + '/movies/genre/documentary',26,artwork + 'docsg.png')
        main.addDir('Drama',base_url + '/movies/genre/drama',26,artwork + 'drama.png')
        main.addDir('Family',base_url + '/movies/genre/family',26,artwork + 'family.png')
        main.addDir('Fantasy',base_url + '/movies/genre/fantasy',26,artwork + 'fantasy.png')
        main.addDir('Film-Noir',base_url + '/movies/genre/film-noir',26,artwork + 'film-noir.png')
        main.addDir('History',base_url + '/movies/genre/history',26,artwork + 'historyg.png')
        main.addDir('Horror',base_url + '/movies/genre/horror',26,artwork + 'horror.png')
        main.addDir('Music',base_url + '/movies/genre/music',26,artwork + 'music.png')
        main.addDir('Musical',base_url + '/movies/genre/musical',26,artwork + 'musical.png')
        main.addDir('Mystery',base_url + '/movies/genre/mystery',26,artwork + 'mystery.png')
        main.addDir('Romance',base_url + '/movies/genre/romance',26,artwork + 'romance.png')
        main.addDir('Sci-Fi',base_url + '/movies/genre/sci-fi',26,artwork + 'sci-fi.png')
        main.addDir('Short',base_url + '/movies/genre/short',26,artwork + 'short.png')
        main.addDir('Sport',base_url + '/movies/genre/sport',26,artwork + 'sport.png')
        main.addDir('Thriller',base_url + '/movies/genre/thriller',26,artwork + 'thriller.png')
        main.addDir('War',base_url + '/movies/genre/war',26,artwork + 'war.png')
        main.addDir('Western',base_url + '/movies/genre/western',26,artwork + 'western.png')

def YEARS():
        main.addDir('2013',base_url + '/movies/year/2013',26,artwork + '2013.png')
        main.addDir('2012',base_url + '/movies/year/2012',26,artwork + '2012.png')
        main.addDir('2011',base_url + '/movies/year/2011',26,artwork + '2011.png')
        main.addDir('2010',base_url + '/movies/year/2010',26,artwork + '2010.png')
        main.addDir('2009',base_url + '/movies/year/2009',26,artwork + '2009.png')
        main.addDir('2008',base_url + '/movies/year/2008',26,artwork + '2008.png')
        main.addDir('2007',base_url + '/movies/year/2007',26,artwork + '2007.png')
        main.addDir('2006',base_url + '/movies/year/2006',26,artwork + '2006.png')
        main.addDir('2005',base_url + '/movies/year/2005',26,artwork + '2005.png')
        main.addDir('2004',base_url + '/movies/year/2004',26,artwork + '2004.png')
        main.addDir('2003',base_url + '/movies/year/2003',26,artwork + '2003.png')
        main.addDir('2002',base_url + '/movies/year/2002',26,artwork + '2002.png')
        main.addDir('2001',base_url + '/movies/year/2001',26,artwork + '2001.png')
        main.addDir('2000',base_url + '/movies/year/2000',26,artwork + '2000.png')
        main.addDir('1999',base_url + '/movies/year/1999',26,artwork + '1999.png')
        main.addDir('1998',base_url + '/movies/year/1998',26,artwork + '1998.png')
        main.addDir('1997',base_url + '/movies/year/1997',26,artwork + '1997.png')
        main.addDir('1996',base_url + '/movies/year/1996',26,artwork + '1996.png')
        main.addDir('1995',base_url + '/movies/year/1995',26,artwork + '1995.png')
        main.addDir('1994',base_url + '/movies/year/1994',26,artwork + '1994.png')
        main.addDir('1993',base_url + '/movies/year/1993',26,artwork + '1993.png')
        main.addDir('1992',base_url + '/movies/year/1992',26,artwork + '1992.png')
        main.addDir('1991',base_url + '/movies/year/1991',26,artwork + '1991.png')
        main.addDir('1990',base_url + '/movies/year/1990',26,artwork + '1990.png')

def INDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href=\'(.+?)\'>\r\n\t\t<img class=\'movie_img\' src=\'(.+?)\' alt=\'(.+?)\' />').findall(link)
        np=re.compile('class="pagination_next"><a class="pagination_link" href="(.+?)"></a></span>').findall(link)
        if len(np) > 0:
                np_url = np[0]
                next_page = base_url + np_url
                main.addDir('Next Page',next_page,26,artwork + 'next.png')
        for url,thumbnail,name in match:
                url = base_url + url

                try:
                        main.addMDir(name,url,27,thumbnail,'')
                except:
                        continue
                
        main.AUTOVIEW('movies')

def VIDEOLINKS(name,url,thumb):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('href="/movies/ext/(.+?)"').findall(link)
        for num in match:
                url = base_url + '/movies/ext/' + num
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                url = response.geturl()

                if url:
                        hmf = urlresolver.HostedMediaFile(url)
                        if hmf:
                                host = hmf.get_host()
                                hthumb = main.GETHOSTTHUMB(host)
                                try:
                                        main.addHDir(name,url,9,thumb,hthumb)
                                except:
                                        continue

def SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = search.replace(' ','+')
                
                url = base_url + 'index.php?s=' + search 
                
                INDEX(url)

