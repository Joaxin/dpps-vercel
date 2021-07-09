from django.shortcuts import render
from .scripts.neteaseMusicAPI import song_infos,album_infos,playlist_infos
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
import re


def netease_song(request):
    return render(request, 'netease_id_song.html')

def netease_album(request):
    return render(request, 'netease_id_album.html')

def netease_playlist(request):
    return render(request, 'netease_id_playlist.html')

def music_url_tools(request):
    return render(request, 'netease_tools.html')

def netease_infos_song(request):
    sid = request.GET['sid']
    print(sid)
    now = datetime.now()
    pattern = re.compile('.*https?:\/\/(y\.)?music\.163\.com\/(#\/|m\/)?(song\?id=|song\/)(\d+)(&|\?|\/\?)?(userid=\d+)?.*', re.S)
    if re.search("^(\d+)$", sid):
        sid = re.search("^(\d+)$", sid).group(1)
    elif re.search(pattern, sid):
        sid = re.search(pattern, sid).group(4)
    ## https://music.163.com/#/song?id=192316 有#的会无法正常解析，会解析成https://music.163.com/
    ## 当url中出现"#"号时，"#"及其后面的字符串都会被忽略，不会被发送到服务器，因为浏览器将一个url视为一个html页面
    ## The "#" character marks inline anchors (links within the same page) in a URL, so the browser will never send it to Django.
    ## SEE https://en.wikipedia.org/wiki/Percent-encoding
    else:
        html = f'''
	    <html>
	        <body>
	            <h1>非法的URL或ID！</h1>
	        </body>
	    </html>
	    '''
        return HttpResponse(html)

    netease_infos_song = song_infos(sid)
    if netease_infos_song:
        return render(request, 'netease_infos_song.html', {'song_infos': netease_infos_song})
    else:
        now = datetime.now()
        html = f'''
	    <html>
	        <body>
	            <h1>无效的歌曲ID! 请访问<a href="http://music.163.com/song?id={sid}" target="_blank">http://music.163.com/song?id={sid}</a></h1>
	            <p>The current time is { now }.</p>
	        </body>
	    </html>
	    '''
        return HttpResponse(html)

def netease_infos_album(request):
    aid = request.GET['aid']
    print(aid)
    now = datetime.now()
    pattern = re.compile('.*https?:\/\/(y\.)?music\.163\.com\/(#\/|m\/)?(album\?id=|album\/)(\d+)(&|\?|\/\?)?(userid=\d+)?.*', re.S)
    if re.search("^(\d+)$", aid):
        aid = re.search("^(\d+)$", aid).group(1)
    elif re.search(pattern, aid):
        aid = re.search(pattern, aid).group(4)
    else:
        html = f'''
	    <html>
	        <body>
	            <h1>非法的URL或ID！</h1>
	        </body>
	    </html>
	    '''
        return HttpResponse(html)

    netease_infos_album_ = album_infos(aid)
    if netease_infos_album:
        return render(request, 'netease_infos_album.html', {'album_infos': netease_infos_album_})
    else:
        now = datetime.now()
        html = f'''
	    <html>
	        <body>
	            <h1>无效的专辑ID! 请访问<a href="http://music.163.com/album?id={aid}" target="_blank">http://music.163.com/album?id={aid}</a></h1>
	            <p>The current time is { now }.</p>
	        </body>
	    </html>
	    '''
        return HttpResponse(html)

def netease_infos_playlist(request):
    pid = request.GET['pid']
    print(pid)
    now = datetime.now()
    pattern = re.compile('.*https?:\/\/(y\.)?music\.163\.com\/(#\/|m\/)?(playlist\?id=|playlist\/)(\d+)(&|\?|\/\?)?(userid=\d+)?.*', re.S)
    if re.search("^(\d+)$", pid):
        pid = re.search("^(\d+)$", pid).group(1)
    elif re.search(pattern, pid):
        pid = re.search(pattern, pid).group(4)
    else:
        html = f'''
        <html>
            <body>
                <h1>非法的URL或ID！</h1>
            </body>
        </html>
        '''
        return HttpResponse(html)

    netease_infos_playlist = playlist_infos(pid)
    if netease_infos_playlist:
        return render(request, 'netease_infos_playlist.html', {'playlist_infos': netease_infos_playlist})
    else:
        now = datetime.now()
        html = f'''
        <html>
            <body>
                <h1>无效的歌单ID! 请访问<a href="http://music.163.com/playlist?id={pid}" target="_blank">http://music.163.com/playlist?id={pid}</a></h1>
                <p>The current time is { now }.</p>
            </body>
        </html>
        '''
        return HttpResponse(html)

def about(request):
    return render(request, 'about.html')
