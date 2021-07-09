from pyncm import apis
from pyncm import utils
import time
import re

## Pyncm From https://github.com/kitUIN/pyncm
## API https://github.com/greats3an/pyncm/wiki

def song_infos(song_id):
    sg_infos = {}
    try:
        song_infos = apis.track.GetTrackDetail(song_id)
        artists = {"name":[],"aname":[],"url":[]}
        for ar in song_infos['songs'][0]['ar']:
            artists["name"].append(ar["name"])
            an = ar.get("alias","")
            if isinstance(an, list):
                an = ",".join(an)
            artists["aname"].append(an)  ## 艺术家别名
            ## https://music.163.com/#/artist?id=17309 艺术家URL
            artists["url"].append("https://music.163.com/artist?id=" + str(ar.get("id","")))
        artists2 = list(zip(*[artists[key] for key in artists]))
        artists = []
        artists_id = []
        for ar in song_infos['songs'][0]['ar']:
            artists.append(ar["name"])
            if ar["id"]:
                artists_id.append(ar["id"])
        artists = "/".join(artists)
        title = song_infos['songs'][0]['name']
        sg_infos["artists"] = artists
        sg_infos["artists2"] = artists2
        sg_infos["title"] = title
        sg_infos["song_id"] = song_id
        sg_infos["song_title"] = artists +" - "+ title ## 歌曲信息
        sg_infos["song_title_"] = re.sub(r"[\(\[（].*?[\)\]）]", "", sg_infos["song_title"]) ## 歌曲信息去括号
        sg_infos["song_album_id"] =  str(song_infos['songs'][0]['al']["id"])  # 专辑ID
        
        album_infos = apis.album.GetAlbumInfo(sg_infos["song_album_id"])
        sg_infos["song_album"] =  song_infos['songs'][0]['al']["name"]  ## 专辑名称
        sg_infos["song_album_url"] =  "http://music.163.com/album?id=" + sg_infos["song_album_id"] ## 专辑URL
        sg_infos["song_album_pic"] = song_infos['songs'][0]['al']["picUrl"]  ## 专辑图片
        sg_infos["song_url"] = "http://music.163.com/song?id=" + str(song_id)  ## 歌曲URL
        sg_infos["song_mp3"] = "http://music.163.com/song/media/outer/url?id=" + str(song_id) + ".mp3"  ## 歌曲MP3
        ## 专辑发行时间
        sg_infos["song_album_publishTime"] = time.strftime("%Y-%m-%d",time.localtime(album_infos['album']['publishTime']/1000))
        sg_infos["song_lyric_url"] = ""
        song_lyric = apis.track.GetTrackLyrics(song_id, lv=-1, tv=-1, rv=-1)
        if song_lyric.get('nolyric'):
            sg_infos["song_lyric"]  = "纯音乐，请欣赏"
        elif song_lyric['lrc']:
            sg_infos["song_lyric_url"] = "https://music.163.com/api/song/lyric?id=" + str(song_id)  + "&lv=1&kv=1&tv=-1"
            sg_infos["song_lyric"]  = song_lyric['lrc']['lyric']
            lys = utils.lrcparser.LrcParser(sg_infos["song_lyric"])
            ## 歌词格式 {0.0: [('00:00.000', ' 作词 : 月吟诗')],1.0: [('00:01.000', ' 作曲 : 月吟诗')],..}
            sg_infos["song_lyric_dict"]  = dict(lys.lyrics_sorted)
            # for item in lyricss:
            #     print(lyricss[item][0][1])
        else:
            sg_infos["song_lyric"] = ""
        return(sg_infos)
    except:
        return(sg_infos)

def playlist_infos(playlist_id):
    playlist_infos = apis.playlist.GetPlaylistInfo(playlist_id)
    pl_infos = {}
    try:
        pl_infos["playlist"]={}
        pl_infos["playlist"]["playlist_url"] = "http://music.163.com/playlist?id=" + str(playlist_infos["playlist"]["id"])  ## 歌单URL
        pl_infos["playlist"]["playlist_name"] = playlist_infos["playlist"]["name"]  ## 歌单名称
        pl_infos["playlist"]["playlist_coverImgUrl"] = playlist_infos["playlist"]["coverImgUrl"] ## 歌单封面
        pl_infos["playlist"]["playlist_creator"] = playlist_infos["playlist"]["creator"]["nickname"]  ## 歌单作者
        pl_infos["playlist"]["playlist_creator_backgroundUrl"] = playlist_infos["playlist"]["creator"]["backgroundUrl"]  ## 歌单创建者背景
        pl_infos["playlist"]["playlist_creator_signature"] = playlist_infos["playlist"]["creator"]["signature"]  ## 歌单作者前面
        pl_infos["playlist"]["playlist_creator_avatarUrl"] = playlist_infos["playlist"]["creator"]["avatarUrl"]  ## 歌单创建者头像
        pl_infos["playlist"]["playlist_creator_id"] = playlist_infos["playlist"]["userId"] ## 歌单作者ID
        pl_infos["playlist"]["playlist_description"] = playlist_infos['playlist']["description"]  ## 歌单简介
        pl_infos["playlist"]["playlist_playCount"] = playlist_infos['playlist']["playCount"]  ## 歌单播放量
        pl_infos["playlist"]["playlist_subscribedCount"] = playlist_infos['playlist']["subscribedCount"]  ## 歌单收藏量
        pl_infos["playlist"]["playlist_tags"] = playlist_infos['playlist']["tags"]  ## 歌单简介
        pl_infos["playlist"]["playlist_createTime"] = time.strftime("%Y-%m-%d",time.localtime(playlist_infos['playlist']['createTime']/1000)) ## 歌单创建时间
        pl_infos["playlist"]["playlist_updateTime"] = time.strftime("%Y-%m-%d",time.localtime(playlist_infos['playlist']['updateTime']/1000)) ## 歌单更新时间
        pl_infos["tracks"] = {}
        for i,pl in enumerate(playlist_infos["playlist"]['trackIds']):
            song_infos = apis.track.GetTrackDetail(pl['id'])
            artists = {"name":[],"aname":[],"url":[]}
            for ar in song_infos['songs'][0]['ar']:
                artists["name"].append(ar["name"])
                an = ar.get("alias","")
                if isinstance(an, list):
                    an = ",".join(an)
                artists["aname"].append(an)  ## 艺术家别名
                ## https://music.163.com/#/artist?id=17309 艺术家URL
                artists["url"].append("https://music.163.com/artist?id=" + str(ar.get("id","")))
            artists2 = list(zip(*[artists[key] for key in artists]))
            artists_name = "/".join(artists["name"])
            title = song_infos['songs'][0]['name']
            sg_infos = {}
            sg_infos["artists"] = artists
            sg_infos["artists2"] = artists2
            sg_infos["artists_name"] = artists_name
            sg_infos["title"] = title
            sg_infos["song_title"] = artists_name + " - "+ title  ## 歌曲信息
            sg_infos["song_id"] =  pl["id"]  ## 歌曲ID
            sg_infos["song_album"] =  song_infos['songs'][0]['al']["name"]   ## 专歌曲辑名称
            sg_infos["song_album_pic"] =  song_infos['songs'][0]['al']["picUrl"]   ## 歌曲专辑图片
            sg_infos["song_url"] = "http://music.163.com/song?id=" + str(pl["id"])  ## 歌曲URL
            sg_infos["song_mp3"] = "http://music.163.com/song/media/outer/url?id=" + str(pl["id"])  + ".mp3"   ## 歌曲MP3
            pl_infos["tracks"][i] = sg_infos
            pl_infos["tracks"][i]["idx"] = i + 1
        ##  查看更多内容，请下载客户端
        # for i,pl in enumerate(playlist_infos["playlist"]['tracks']):
        #     artists = {"name":[],"aname":[],"url":[]}
        #     for ar in pl['ar']:
        #         artists["name"].append(ar["name"])
        #         an = ar.get("alia","")
        #         if isinstance(an, list):
        #             an = ",".join(an)
        #         artists["aname"].append(an)  ## 艺术家别名
        #         ## https://music.163.com/#/artist?id=17309 艺术家URL
        #         artists["url"].append("https://music.163.com/artist?id=" + str(ar.get("id","")))
        #     artists2 = list(zip(*[artists[key] for key in artists]))
        #     ## [('阿南亮子', 'Anan Ryoko', 'https://music.163.com/artist?id=16069'),('Nicky Guiland', '', 'https://music.163.com/artist?id=234474')]
        #     # e.g. {'name': ['阿南亮子', 'Nicky Guiland'], 'aname': ['Anan Ryoko', ''], 'url': ['https://music.163.com/artist?id=16069', 'https://music.163.com/artist?id=234474']}
        #     artists_name = "/".join(artists["name"])
        #     title = pl['name']
        #     sg_infos = {}
        #     sg_infos["artists"] = artists
        #     sg_infos["artists2"] = artists2
        #     sg_infos["artists_name"] = artists_name
        #     sg_infos["title"] = title
        #     sg_infos["song_title"] = artists_name + " - "+title  ## 歌曲信息
        #     sg_infos["song_id"] =  pl["id"]  ## 歌曲ID
        #     sg_infos["song_album"] =  pl['al']["name"]  ## 专歌曲辑名称
        #     sg_infos["song_album_tns"] =  ",".join(pl['al'].get("tns",""))  ## 歌曲专辑翻译
        #     sg_infos["song_album_pic"] =  pl['al']["picUrl"]  ## 歌曲专辑图片
        #     sg_infos["song_url"] = "http://music.163.com/song?id=" + str(pl["id"])  ## 歌曲URL
        #     sg_infos["song_mp3"] = "http://music.163.com/song/media/outer/url?id=" + str(pl["id"])  + ".mp3"   ## 歌曲MP3
        #     pl_infos["tracks"][i] = sg_infos
        #     pl_infos["tracks"][i]["idx"] = i + 1
        return(pl_infos)
    except:
        return(pl_infos)

def album_infos(album_id):
    album_infos = apis.album.GetAlbumInfo(album_id)
    al_infos = {}
    try:
        al_infos["album"]={}
        al_infos["album"]["album_url"] = "http://music.163.com/album?id=" + str(album_infos['songs'][0]["al"]["id"]) ## 专辑URL
        al_infos["album"]["album_name"] = album_infos['album']["name"]  ## 专辑名称
        al_infos["album"]["album_picUrl"] = album_infos['album']['picUrl']   ## 专辑图片
        al_infos["album"]["album_publishTime"] = time.strftime("%Y-%m-%d",time.localtime(album_infos['album']['publishTime']/1000)) ## 专辑发行时间
        al_infos["album"]["album_description"] = album_infos['album']["description"]  ## 专辑简介
        al_infos["album"]["album_subType"] = album_infos['album']['subType']  ## 专辑介质
        al_infos["album"]["album_company"] = album_infos['album']['company']  ## 发行公司
        artist_name = album_infos['album']['artist']['name'] ## 艺术家
        al_infos["album"]["album_artists"] = artist_name
        al_infos["album"]["album_artists_i"] = artist_name + ",".join(album_infos['album']['artist'].get('alias',""))  ## 艺术家
        al_infos["album"]["album_artists_img"] = album_infos['album']['artist']['picUrl']  ## 艺术家图片
        al_infos["album"]["album_artists_id"] = album_infos['album']['artist']['id']  ## 艺术家ID
        al_infos["album"]["album_paid"] = album_infos['album']['paid'] ## 是否为付费专辑
        al_infos["songs"] = {}
        for i,pl in enumerate(album_infos["songs"]):
            artists = {"name":[],"aname":[],"url":[]}
            for ar in pl['ar']:
                artists["name"].append(ar["name"])
                an = ar.get("alia","")
                if isinstance(an, list):
                    an = ",".join(an)
                artists["aname"].append(an)  ## 艺术家别名
                ## https://music.163.com/#/artist?id=17309 艺术家URL
                artists["url"].append("https://music.163.com/artist?id=" + str(ar.get("id","")))
            artists2 = list(zip(*[artists[key] for key in artists]))
            ## [('阿南亮子', 'Anan Ryoko', 'https://music.163.com/artist?id=16069'),('Nicky Guiland', '', 'https://music.163.com/artist?id=234474')]
            # e.g. {'name': ['阿南亮子', 'Nicky Guiland'], 'aname': ['Anan Ryoko', ''], 'url': ['https://music.163.com/artist?id=16069', 'https://music.163.com/artist?id=234474']}
            artists_name = "/".join(artists["name"])
            title = pl['name']
            sg_infos = {}
            sg_infos["artists"] = artists
            sg_infos["artists2"] = artists2
            sg_infos["artists_name"] = artists_name
            sg_infos["title"] = title
            sg_infos["song_title"] = artists_name + " - "+title  ## 歌曲信息
            sg_infos["song_id"] =  pl["id"]  ## 歌曲ID
            sg_infos["song_album"] =  pl['al']["name"]  ## 专歌曲辑名称
            sg_infos["song_album_tns"] =  ",".join(pl['al'].get("tns",""))  ## 歌曲专辑翻译
            sg_infos["song_album_pic"] =  pl['al']["picUrl"]  ## 歌曲专辑图片
            sg_infos["song_url"] = "http://music.163.com/song?id=" + str(pl["id"])  ## 歌曲URL
            sg_infos["song_mp3"] = "http://music.163.com/song/media/outer/url?id=" + str(pl["id"])  + ".mp3"   ## 歌曲MP3
            al_infos["songs"][i] = sg_infos
            al_infos["songs"][i]["idx"] = i + 1
        return(al_infos)
    except:
        return(al_infos)
if __name__ == '__main__':
    pass