from django.shortcuts import render
from .scripts.neteaseMusicAPI import song_infos,album_infos,playlist_infos,playlist_infos_compare
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

def netease_playlist_compare(request):
    # print(request.GET)
    if request.GET:
        pid1 = request.GET['pid1']
        pid2 = request.GET['pid2']
        quick_mode = request.GET.get('quick_mode',None)
        similar_mode = request.GET.get('similar_mode',None)

        pattern = re.compile('.*https?:\/\/(y\.)?music\.163\.com\/(#\/|m\/)?(playlist\?id=|playlist\/)(\d+)(&|\?|\/\?)?(userid=\d+)?.*', re.S)
        if re.search("^(\d+)$", pid1):
            pid1 = re.search("^(\d+)$", pid1).group(1)
        elif re.search(pattern, pid1):
            pid1 = re.search(pattern, pid1).group(4)
        else:
            html = f'''
            <html>
                <body>
                    <h1>非法的URL或ID！(请检查歌单ID1)</h1>
                </body>
            </html>
            '''
            return HttpResponse(html)

        if re.search("^(\d+)$", pid2):
            pid2 = re.search("^(\d+)$", pid2).group(1)
        elif re.search(pattern, pid2):
            pid2 = re.search(pattern, pid2).group(4)
        else:
            html = f'''
            <html>
                <body>
                    <h1>非法的URL或ID！(请检查歌单ID2)</h1>
                </body>
            </html>
            '''
            return HttpResponse(html)
        
        if similar_mode == "on":
            similar_mode = True
        else:
            similar_mode = False
        
        print(similar_mode)
        if quick_mode == "on":
            netease_infos_playlist_compare = playlist_infos_compare(pid1,pid2,simplified = True,similar_mode = similar_mode)
            quick_mode = 0
        else:
            netease_infos_playlist_compare = playlist_infos_compare(pid1,pid2,simplified = False,similar_mode = similar_mode)
            quick_mode = 1
        
        if netease_infos_playlist_compare:
            return render(request, 'netease_id_playlist_compare.html', 
            {'pl_1not2': netease_infos_playlist_compare[0],'pl_2not1': netease_infos_playlist_compare[1],
            'playlist':{'plname1':netease_infos_playlist_compare[2],'plname2':netease_infos_playlist_compare[3],"plen1":netease_infos_playlist_compare[4],"plen2":netease_infos_playlist_compare[5]},
            'pl_12':netease_infos_playlist_compare[6],
            'quick_mode':quick_mode,
            "pid":{"pid1":pid1,"pid2":pid2}})
        else:
            html = f'''
            <html>
                <body>
                    <h1>无效的歌单ID! 请访问<a href="http://music.163.com/playlist?id={pid1}" target="_blank">http://music.163.com/playlist?id={pid1}</a></h1>或者
                    <h1>无效的歌单ID! 请访问<a href="http://music.163.com/playlist?id={pid2}" target="_blank">http://music.163.com/playlist?id={pid2}</a></h1>检查
                </body>
            </html>
            '''
            return HttpResponse(html)
    else:
        return render(request, 'netease_id_playlist_compare.html')

