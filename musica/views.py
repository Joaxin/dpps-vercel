from django.shortcuts import render
from .scripts.neteaseMusicAPI import song_infos
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
from urllib.parse import quote
import re


def home(request):
    return render(request, 'netease_id.html')


def netease_infos(request):
    sid = quote(request.GET['sid'])
    now = datetime.now()
    pattern = re.compile('song%3Fid%3D(\d+).*', re.S)
    if re.search("^(\d+)$", sid):
        sid = re.search("^(\d+)$", sid).group(1)
    elif re.search(pattern, sid):
        sid = re.search(pattern, sid).group(1)
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

    netease_song_infos = song_infos(sid)
    if netease_song_infos:
        return render(request, 'netease_infos.html', {'song_infos': netease_song_infos})
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


def about(request):
    return render(request, 'about.html')
