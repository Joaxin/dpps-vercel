from pyncm import apis
from pyncm import utils
import time

## Pyncm From https://github.com/kitUIN/pyncm
## API https://github.com/greats3an/pyncm/wiki
def song_infos(song_id):
    sg_infos = {}
    try:
        song_infos = apis.track.GetTrackDetail(song_id)
        artists = []
        artists_id = []
        for ar in song_infos['songs'][0]['ar']:
            artists.append(ar["name"])
            if ar["id"]:
                artists_id.append(ar["id"])
        artists = "/".join(artists)
        title = song_infos['songs'][0]['name']
        sg_infos["artists"] = artists
        sg_infos["title"] = title
        sg_infos["song_id"] = song_id
        sg_infos["song_title"] = artists +" - "+ title ## 歌曲信息
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
    pl_infos["playlist"]={}
    pl_infos["playlist"]["playlist_url"] = "http://music.163.com/playlist?id=" + str(playlist_infos["playlist"]["id"])
    pl_infos["playlist"]["playlist_name"] = playlist_infos["playlist"]["name"]
    pl_infos["playlist"]["playlist_coverImgUrl"] = playlist_infos["playlist"]["coverImgUrl"]
    pl_infos["playlist"]["playlist_creator"] = playlist_infos["playlist"]["creator"]["nickname"]
    pl_infos["playlist"]["playlist_creator_url"] = "https://music.163.com/#/user/home?id" + str(playlist_infos["playlist"]["userId"])
    pl_infos["songs"] = {}
    for i,pl in enumerate(playlist_infos["playlist"]['tracks']):
        artists = []
        for ar in pl['ar']:
            artists.append(ar["name"])
        artists = "/".join(artists)
        title = pl['name']
        sg_infos = {}
        sg_infos["artists"] = artists
        sg_infos["title"] = title
        sg_infos["歌曲信息"] = artists + " - "+title
        sg_infos["歌曲ID"] =  pl["id"] 
        sg_infos["歌曲专辑"] =  pl['al']["name"] 
        sg_infos["歌曲图片"] =  pl['al']["picUrl"] 
        sg_infos["歌曲URL"] = "http://music.163.com/song?id=" + str(pl["id"])
        sg_infos["歌曲MP3"] = "http://music.163.com/song/media/outer/url?id=" + str(pl["id"])  + ".mp3"
        pl_infos["songs"][i] = sg_infos
    return(pl_infos)

def album_infos(album_id):
    album_infos = apis.album.GetAlbumInfo(album_id)
    al_infos = {}
    al_infos["album"]={}
    al_infos["album"]["album_url"] = "http://music.163.com/album?id=" + str(album_infos['songs'][0]["al"]["id"])
    al_infos["album"]["album_name"] = album_infos['album']["name"]
    al_infos["album"]["album_picUrl"] = album_infos['album']['picUrl']
    al_infos["album"]["album_publishTime"] = time.strftime("%Y-%m-%d",time.localtime(album_infos['album']['publishTime']/1000))
    al_infos["album"]["album_company"] = album_infos['album']['company']
    al_infos["album"]["album_artists"] = album_infos['album']['artist']['name']
    al_infos["album"]["album_artists_img"] = album_infos['album']['artist']['picUrl']
    al_infos["songs"] = {}
    for i,pl in enumerate(album_infos["songs"]):
        artists = []
        for ar in pl['ar']:
            artists.append(ar["name"])
        artists = "/".join(artists)
        title = pl['name']
        sg_infos = {}
        sg_infos["artists"] = artists
        sg_infos["title"] = title
        sg_infos["歌曲信息"] = artists + " - "+title
        sg_infos["歌曲ID"] =  pl["id"] 
        sg_infos["歌曲专辑"] =  pl['al']["name"] 
        sg_infos["歌曲图片"] =  pl['al']["picUrl"] 
        sg_infos["歌曲URL"] = "http://music.163.com/song?id=" + str(pl["id"])
        sg_infos["歌曲MP3"] = "http://music.163.com/song/media/outer/url?id=" + str(pl["id"])  + ".mp3"
        al_infos["songs"][i] = sg_infos
    return(al_infos)

if __name__ == '__main__':
    ID = ''
    album_douban_crawl(ID)