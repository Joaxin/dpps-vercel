from django.shortcuts import render
from .scripts.neteaseMusicAPI import song_infos
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
import re


def home(request):
    return render(request, 'netease_id.html')


def netease_infos(request):
    sid = request.GET['sid']
    now = datetime.now()
    pattern = re.compile('song\?id=(\d+).*', re.S)
    if re.search("^(\d+)$", sid):
        sid = re.search("^(\d+)$", sid).group(1)
    elif re.search(pattern, sid):
        sid = re.search(pattern, sid).group(1)
    else:
        html = f'''
	    <html>
	        <body>
	            <h1>非法输入！/h1>
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
