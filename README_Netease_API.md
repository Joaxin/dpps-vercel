Pyncm From https://github.com/greats3an/pyncm

![Logo](https://github.com/greats3an/pyncm/raw/master/demos/_logo.png)

> NeteaseCloudMusic APIs for Python 3.x 适用于 Python 3 的网易云音乐 API
>
> ```
> pip install pyncm
> from pyncm import apis
> ```

API https://github.com/greats3an/pyncm/wiki

## API测试

### Song

http://music.163.com/song?id=427142070

![](https://i.postimg.cc/7Zn1Vgbr/image.png)

```python
apis.track.GetTrackDetail(427142070)
// 正常播放，非VIP
apis.track.GetTrackDetail(3356858653)
// 无版权，非VIP
```

```
{'songs': [{'name': 'Lemon',
   'id': 427142070,
   'pst': 0,
   't': 0,
   'ar': [{'id': 12108155, 'name': 'Tülpa', 'tns': [], 'alias': []}],
   'alia': [],
   'pop': 95.0,  --------疑似热度
   'st': 0,
   'rt': None,
   'fee': 0,
   'v': 2, --------- 2或4或39 未知
   'crbt': None,
   'cf': '',
   'al': {'id': 34839317,
    'name': 'Lemon',
    'picUrl': 'https://p2.music.126.net/djvRTkG93l1mkW4m-rkZ7g==/3417282151060043.jpg',  ----------专辑封面地址
    'tns': [],
    'pic': 3417282151060043},
   'dt': 315555,
   'h': {'br': 320000, 'fid': 0, 'size': 12624501, 'vd': 414.0},----音质和文件大小
   'm': {'br': 192000, 'fid': 0, 'size': 7574718, 'vd': 2421.0},
   'l': {'br': 128000, 'fid': 0, 'size': 5049826, 'vd': -2.0},
   'a': None,
   'cd': '1',
   'no': 1,
   'rtUrl': None,
   'ftype': 0,
   'rtUrls': [],
   'djId': 0,
   'copyright': 0, ----------版权0(有版权)或1(无版权)和2(无版权，有其他版本)，比如有单独参数比如：'noCopyrightRcmd': {'type': 2, 'typeDesc': '其它版本可播', 'songId': None}
   's_id': 0,
   'mark': 262144,
   'originCoverType': 0,
   'originSongSimpleData': None,
   'resourceState': True,
   'single': 0,
   'noCopyrightRcmd': None,
   'rtype': 0,
   'rurl': None,
   'mst': 9,
   'cp': 0,
   'mv': 0,
   'publishTime': 1447862400007}],
 'privileges': [{'id': 427142070,
   'fee': 0,
   'payed': 0, ---是否付费，0为免费
   'st': 0,
   'pl': 320000,
   'dl': 320000,
   'sp': 7,
   'cp': 1,
   'subp': 1,
   'cs': False,
   'maxbr': 320000,
   'fl': 320000,
   'toast': False,
   'flag': 0,
   'preSell': False,
   'playMaxbr': 320000,
   'downloadMaxbr': 320000,
   'rscl': None,
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'chargeInfoList': [{'rate': 128000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 192000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 320000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 999000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1}]}],
 'code': 200}
```



### Album

```
apis.album.GetAlbumInfo(2084576)
```

https://music.163.com/#/album?id=2084576

> 有版权，非VIP

![](https://i.postimg.cc/WzHvkFLB/image.png)

```json
{'resourceState': True,
 'songs': [{'rtUrls': [],
   'ar': [{'id': 16069, 'name': '阿南亮子', 'alia': ['Anan Ryoko']},
    {'id': 69169, 'name': 'Michelle Shaprow'}],
   'al': {'id': 2084576,
    'name': 'Eternal Light',
    'picUrl': 'https://p2.music.126.net/HpNhvHFZXTLwrVXMT7WP8g==/109951163028848374.jpg',
    'tns': ['永恒之光'],
    'pic_str': '109951163028848374',
    'pic': 109951163028848374},
   'st': 1,    ---- 值为1或-1
   'noCopyrightRcmd': None,
   'rtype': 0,
   'rurl': None,
   'pst': 0,
   't': 0,
   'pop': 25.0,  ------- 疑似热度
   'rt': '',
   'mst': 9,
   'cp': 663018,
   'crbt': None,
   'cf': '',
   'dt': 267293,
   'h': {'br': 320000, 'fid': 0, 'size': 10694574, 'vd': -16300.0},
   'l': {'br': 128000, 'fid': 0, 'size': 4277856, 'vd': -12000.0},
   'rtUrl': None,
   'ftype': 0,
   'no': 1,
   'fee': 0,
   'djId': 0,
   'v': 125,
   'alia': [],
   'mv': 0,
   'cd': '1',
   'a': None,
   'm': {'br': 192000, 'fid': 0, 'size': 6416762, 'vd': -13700.0},
   'name': 'Sure As The Sunshine',
   'id': 22712178,
   'privilege': {'id': 22712178,
    'fee': 0,
    'payed': 0,
    'st': 0,
    'pl': 320000,
    'dl': 999000,
    'sp': 7,
    'cp': 1,
    'subp': 1,
    'cs': False,
    'maxbr': 999000,
    'fl': 320000,
    'toast': False,
    'flag': 256,
    'preSell': False,
    'playMaxbr': 999000,
    'downloadMaxbr': 999000,
    'rscl': None,
    'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
    'chargeInfoList': [{'rate': 128000,
      'chargeUrl': None,
      'chargeMessage': None,
      'chargeType': 0},
     {'rate': 192000,
      'chargeUrl': None,
      'chargeMessage': None,
      'chargeType': 0},
     {'rate': 320000,
      'chargeUrl': None,
      'chargeMessage': None,
      'chargeType': 0},
     {'rate': 999000,
      'chargeUrl': None,
      'chargeMessage': None,
      'chargeType': 1}]},
   'eq': 'megabass'},
 ...
],
 'code': 200,
 'album': {'songs': [],
  'paid': False,
  'onSale': False,
  'mark': 0,
  'blurPicUrl': 'https://p2.music.126.net/HpNhvHFZXTLwrVXMT7WP8g==/109951163028848374.jpg',
  'companyId': 0,
  'artists': [{'img1v1Id': 18686200114669622,
    'topicPerson': 0,
    'alias': [],
    'picId': 0,
    'musicSize': 0,
    'albumSize': 0,
    'briefDesc': '',
    'picUrl': 'https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg',
    'img1v1Url': 'https://p2.music.126.net/VnZiScyynLG7atLIZ2YPkw==/18686200114669622.jpg',
    'followed': False,
    'trans': '',
    'name': '阿南亮子',
    'id': 16069,
    'img1v1Id_str': '18686200114669622'}],
  'alias': [],
  'copyrightId': 0,
  'picId': 109951163028848374,
  'artist': {'img1v1Id': 109951163028853928,
   'topicPerson': 0,
   'alias': ['Anan Ryoko'],
   'picId': 109951163028859256,
   'musicSize': 159,
   'albumSize': 8,
   'briefDesc': '',
   'picUrl': 'https://p2.music.126.net/c_eojivhszSH1aEj2q3p_w==/109951163028859256.jpg',
   'img1v1Url': 'https://p2.music.126.net/Zj-5JgN9JPQSe2WifkvdwQ==/109951163028853928.jpg',
   'followed': False,
   'trans': '',
   'name': '阿南亮子',
   'id': 16069,
   'picId_str': '109951163028859256',
   'img1v1Id_str': '109951163028853928'},
  'briefDesc': '',
  'publishTime': 1307462400007,
  'company': 'Palette Sounds',
  'picUrl': 'https://p2.music.126.net/HpNhvHFZXTLwrVXMT7WP8g==/109951163028848374.jpg',
  'commentThreadId': 'R_AL_3_2084576',
  'pic': 109951163028848374,
  'tags': '',
  'description': 'Cradleの瀬戸智树により才能を开花することとなった女流ピアニスト兼作曲家Anan Ryoko待望の2ndアルバムが完成! 魅惑的でポジティブな歌声を持つオランダの歌姫Giovancaを始め、フェアリーでスウィートな ヴォーカルが 魅力のMichelle Shaprow、オランダが世界に夸るソウルレーベル、キンドレッド・スピリッツが送り出す 女性ヴォーカリストNicky Guiland 、韩国最大のサイトCyworldで総合チャート1位を获得した MC Sniperの客演など超豪华客演阵に、NHK全国放送のドラマ「恋する日本语」に起用された「春の雪」 などANAN RYOKOの天性のメロディと演奏の魅力が詰まった最高杰作!',
  'status': 1,
  'subType': '录音室版',
  'name': 'Eternal Light',
  'id': 2084576,
  'type': '专辑',
  'size': 12,
  'picId_str': '109951163028848374',
  'transNames': ['永恒之光'],
  'info': {'commentThread': {'id': 'R_AL_3_2084576',
    'resourceInfo': {'id': 2084576,
     'userId': -1,
     'name': 'Eternal Light',
     'imgUrl': 'https://p2.music.126.net/HpNhvHFZXTLwrVXMT7WP8g==/109951163028848374.jpg',
     'creator': None,
     'encodedId': None,
     'subTitle': None,
     'webUrl': None},
    'resourceType': 3,
    'commentCount': 182,
    'likedCount': 0,
    'shareCount': 257,
    'hotCount': 7,
    'latestLikedUsers': None,
    'resourceTitle': 'Eternal Light',
    'resourceOwnerId': -1,
    'resourceId': 2084576},
   'latestLikedUsers': None,
   'liked': False,
   'comments': None,
   'resourceType': 3,
   'resourceId': 2084576,
   'commentCount': 182,
   'likedCount': 0,
   'shareCount': 257,
   'threadId': 'R_AL_3_2084576'}}}
```

爬虫结果:

```
{'album': {'album_url': 'http://music.163.com/album?id=2084576',
  'album_name': 'Eternal Light',
  'album_picUrl': 'https://p2.music.126.net/HpNhvHFZXTLwrVXMT7WP8g==/109951163028848374.jpg',
  'album_publishTime': '2011-06-08',
  'album_description': 'Cradleの瀬戸智树により才能を开花することとなった女流ピアニスト兼作曲家Anan Ryoko待望の2ndアルバムが完成! 魅惑的でポジティブな歌声を持つオランダの歌姫Giovancaを始め、フェアリーでスウィートな ヴォーカルが 魅力のMichelle Shaprow、オランダが世界に夸るソウルレーベル、キンドレッド・スピリッツが送り出す 女性ヴォーカリストNicky Guiland 、韩国最大のサイトCyworldで総合チャート1位を获得した MC Sniperの客演など超豪华客演阵に、NHK全国放送のドラマ「恋する日本语」に起用された「春の雪」 などANAN RYOKOの天性のメロディと演奏の魅力が詰まった最高杰作!',
  'album_subType': '录音室版',
  'album_company': 'Palette Sounds',
  'album_artists': '阿南亮子',
  'album_artists_i': '阿南亮子Anan Ryoko',
  'album_artists_img': 'https://p2.music.126.net/c_eojivhszSH1aEj2q3p_w==/109951163028859256.jpg',
  'album_paid': False},
 'songs': {0: {'artists': {'name': ['阿南亮子', 'Michelle Shaprow'],
    'aname': ['Anan Ryoko', ''],
    'url': ['https://music.163.com/artist?id=16069',
     'https://music.163.com/artist?id=69169']},
   'artists_name': '阿南亮子/Michelle Shaprow',
   'title': 'Sure As The Sunshine',
   'song_title': '阿南亮子/Michelle Shaprow - Sure As The Sunshine',
   'song_id': 22712178,
   'song_album': 'Eternal Light',
   'song_album_tns': '永恒之光',
   'song_album_pic': 'https://p1.music.126.net/HpNhvHFZXTLwrVXMT7WP8g==/109951163028848374.jpg',
   'song_url': 'http://music.163.com/song?id=22712178',
   'song_mp3': 'http://music.163.com/song/media/outer/url?id=22712178.mp3',
   'idx': 1},
...
```
### Audio

```python
# https://music.163.com/#/song?id=22712178
apis.track.GetTrackAudio(22712178)
```

```
{'data': [{'id': 22712178,
   'url': 'http://m8.music.126.net/20210706154308/b1e27463d03a4e0582ef497f437b045b/ymusic/e5b3/51cb/1fb7/2ca71af6cb7c487019edbb98ee4d7a18.mp3',
   'br': 320000,
   'size': 10694574,
   'md5': '2ca71af6cb7c487019edbb98ee4d7a18',
   'code': 200,
   'expi': 1200,
   'type': 'mp3',
   'gain': 0.0,
   'fee': 0,
   'uf': None,
   'payed': 0,
   'flag': 256,
   'canExtend': False,
   'freeTrialInfo': None,
   'level': 'exhigh',
   'encodeType': 'mp3',
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'freeTimeTrialPrivilege': {'resConsumable': False,
    'userConsumable': False,
    'type': 0,
    'remainTime': 0},
   'urlSource':
```

### Lyrics

```python
apis.track.GetTrackLyrics(38574759, lv=-1, tv=-1, rv=-1)['nolyric']
# True
```

```python
ly = apis.track.GetTrackLyrics(425065746, lv=-1, tv=-1, rv=-1)['lrc']['lyric']
from pyncm.utils.lrcparser import LrcParser
lys = LrcParser(ly)
lyricss = dict(lys.lyrics_sorted)
for item in lyricss:
    print(lyricss[item][0][1])
# for l in lys:
#     print(l)
```

```
 作词 : 月吟诗
 作曲 : 月吟诗
【天地映雪】——剑网叁七周年苍云门派原创歌曲
演唱/和声：簟画
编曲：簟画 原野婆婆纳
分轨混音：亦北zenia
轻眉映雪 雪落琉璃世界
梦醒在梦的边缘
星辰睁眼 见我拂散狼烟
---
```

```python
lyricss
```

```
{0.0: [('00:00.000', ' 作词 : 月吟诗')],
 1.0: [('00:01.000', ' 作曲 : 月吟诗')],
 27.0: [('00:27.00', '【天地映雪】——剑网叁七周年苍云门派原创歌曲')],
 33.36: [('00:33.36', '演唱/和声：簟画')],
 35.36: [('00:35.36', '编曲：簟画 原野婆婆纳')],
 37.85: [('00:37.85', '分轨混音：亦北zenia')],
 56.74: [('00:56.74', '轻眉映雪 雪落琉璃世界')],
 65.69: [('01:05.69', '梦醒在梦的边缘')],
 73.81: [('01:13.81', '星辰睁眼 见我拂散狼烟')],
 82.13: [('01:22.13', '心越过沧海桑田')],
 91.96: [('01:31.96', '人间几回眸')],
 99.88: [('01:39.88', '江山总是愁')],
 107.84: [('01:47.84', '雁门关外 鼓角喧鸣')],
 114.32: [('01:54.32', '灭虏志未酬 誓死不休')],
 124.26: [('02:04.26', '峥嵘铁骨逐寒流')],
 127.94: [('02:07.94', '盾甲刀魂惊春秋')],
 131.95: [('02:11.95', '哪叹今生岁月久')],
 135.77: [('02:15.77', '愿守一方天地朽')],
 162.11: [('02:42.11', '苍云映雪 雪落千念万劫')],
 169.94: [('02:49.94', '血浸透血的残简')],
 177.69: [('02:57.69', '烽火灼眼 伴我驰骋荒原')],
 185.38: [('03:05.38', '心难咏故园诗篇')],
 195.54: [('03:15.54', '人间几回眸')],
 202.67: [('03:22.67', '江山总是愁')],
 211.57: [('03:31.57', '雁门关外 鼓角喧鸣')],
 218.09: [('03:38.09', '灭虏志未酬 誓死不休')],
 227.91: [('03:47.91', '峥嵘铁骨逐寒流')],
 232.02: [('03:52.02', '盾甲刀魂惊春秋')],
 235.99: [('03:55.99', '哪叹今生岁月久')],
 240.01: [('04:00.01', '愿守一方天地朽')],
 284.07: [('04:44.07', '峥嵘铁骨逐寒流')],
 287.73: [('04:47.73', '盾甲刀魂惊春秋')],
 291.79: [('04:51.79', '哪叹今生岁月久')],
 295.71: [('04:55.71', '愿守一方天地朽')]}
```

### Playlist

```
apis.playlist.GetPlaylistInfo("413889091")
```

```
{'code': 200,
 'relatedVideos': None,
 'playlist': {'id': 413889091,
  'name': '电影配乐中的古典乐章｜正声雅音',
  'coverImgId': 2946691188914673,
  'coverImgUrl': 'https://p1.music.126.net/edYwvhCmV9rOInIGkBqKAQ==/2946691188914673.jpg',
  'coverImgId_str': None,
  'adType': 0,
  'userId': 2445590,
  'createTime': 1467465396093,
  'status': 0,
  'opRecommend': False,
  'highQuality': False,
  'newImported': False,
  'updateTime': 1595912228816,
  'trackCount': 33,
  'specialType': 0,
  'privacy': 0,
  'trackUpdateTime': 1624236857786,
  'commentThreadId': 'A_PL_0_413889091',
  'playCount': 2766836,
  'trackNumberUpdateTime': 1595912228816,
  'subscribedCount': 96810,
  'cloudTrackCount': 0,
  'ordered': True,
  'description': '古典音乐是最早被引入电影的音乐类型之一，自电影诞生初期就相伴于这门现代艺术，古典音乐中的不同乐思能够描述不同的情绪气氛，可以是《时光倒流七十年》里的情意隽永，也可以是《七宗罪》里的忧郁黯然；也可以是《2001：太空漫游》里的庄严宏大。在电影中，古典音乐以其丰富的表现力和深刻的内涵在有声电影中起到了营造气势、 渲染氛围、刻画人物、表述情节、烘托气氛、展现风格、增强影片的戏剧张力等不同的作用，成为电影音乐的一种重要风格流派。\n.\n歌单封面：选自电影《公爵夫人》。\n.\n选曲电影，按歌单顺序排列。\n1.《卢金的防守》\n2.《她比烟花寂寞》\n3.《触不可及》\n4.《怒海争锋》\n5.《文科恋曲》\n6.《钢琴教师》\n7.《土拨鼠之日》\n8.《巴里林登》\n9.《禁闭岛》\n10.《年轻时候》\n11.《穿越大吉岭》\n12.《国王的演讲》\n13.《发条橙》\n14.《走出非洲》\n15.《爱在日落黄昏时》\n16.《七宗罪》\n17.《2001 太空漫游》\n18.《教父3》\n19.《时光倒流七十年》\n20.《公爵夫人》\n21.《刺杀肯尼迪》\n22.《莫扎特传》\n23.《爵士春秋》\n24.《爱情故事》\n25.《危险的月光》\n26.《玻璃情人》\n27.《音乐会》\n28.《海边的曼切斯特》\n29.《大开眼戒》\n30.《纯真年代》\n31.《坠入》\n32.《鸟人》\n33.《美好年代》\n.',
  'tags': ['欧美', '古典', '影视原声'],
  'updateFrequency': None,
  'backgroundCoverId': 0,
  'backgroundCoverUrl': None,
  'titleImage': 0,
  'titleImageUrl': None,
  'englishTitle': None,
  'officialPlaylistType': None,
  'subscribers': [],
  'subscribed': None,
  'creator': {'defaultAvatar': False,
   'province': 1000000,
   'authStatus': 0,
   'followed': False,
   'avatarUrl': 'http://p1.music.126.net/Jrj86gDsmjxYaWG0VuIpNQ==/109951163446003588.jpg',
   'accountStatus': 0,
   'gender': 0,
   'city': 1010000,
   'birthday': -1557561600000,
   'userId': 2445590,
   'userType': 200,
   'nickname': '下一颗巧克力',
   'signature': 'B站：电影蒙太七\n微博：下一颗巧克力ZRY',
   'description': '',
   'detailDescription': '',
   'avatarImgId': 109951163446003588,
   'backgroundImgId': 109951164414271530,
   'backgroundUrl': 'http://p1.music.126.net/IBRjnjTC46NHGV1QxWhNYA==/109951164414271530.jpg',
   'authority': 0,
   'mutual': False,
   'expertTags': ['影视原声', '另类/独立', '欧美'],
   'experts': {'2': '资讯(影视、欧美音乐)'},
   'djStatus': 0,
   'vipType': 11,
   'remarkName': None,
   'authenticationTypes': 1344,
   'avatarDetail': {'userType': 200,
    'identityLevel': 3,
    'identityIconUrl': 'https://p5.music.126.net/obj/wo3DlcOGw6DClTvDisK1/4761340168/ccce/35dd/ab2d/1a7c8ee0f6bb1fc2760cbb570dfee34f.png'},
   'anchor': False,
   'backgroundImgIdStr': '109951164414271530',
   'avatarImgIdStr': '109951163446003588',
   'avatarImgId_str': '109951163446003588'},
  'tracks': [{'name': 'Waltz No. 2 from Jazz Suite No. 2',
    'id': 997889,
    'pst': 0,
    't': 0,
    'ar': [{'id': 27626, 'name': 'Alexandre Desplat', 'tns': [], 'alias': []}],
    'alia': [],
    'pop': 95.0,
    'st': 0,
    'rt': '',
    'fee': 8,
    'v': 83,
    'crbt': None,
    'cf': '',
    'al': {'id': 104390,
     'name': 'The Luzhin Defence (Original Film Soundtrack)',
     'picUrl': 'http://p4.music.126.net/hwzXqzMtix7Qs2P5dbfxbg==/18280480323974794.jpg',
     'tns': [],
     'pic_str': '18280480323974794',
     'pic': 18280480323974794},
    'dt': 233560,
    'h': {'br': 320000, 'fid': 0, 'size': 9344566, 'vd': 1921.0},
    'm': {'br': 192000, 'fid': 0, 'size': 5606757, 'vd': 3375.0},
    'l': {'br': 128000, 'fid': 0, 'size': 3737853, 'vd': 1691.0},
    'a': None,
    'cd': '1',
    'no': 16,
    'rtUrl': None,
    'ftype': 0,
    'rtUrls': [],
    'djId': 0,
    'copyright': 2,
    's_id': 0,
    'mark': 401408,
    'originCoverType': 0,
    'originSongSimpleData': None,
    'single': 0,
    'noCopyrightRcmd': None,
    'mst': 9,
    'cp': 564029,
    'mv': 0,
    'rtype': 0,
    'rurl': None,
    'publishTime': 1209312000000},
   ...
  ],
  'videoIds': None,
  'videos': None,
  'trackIds': [{'id': 997889,
    'v': 83,
    't': 0,
    'at': 1508074644276,
    'alg': None,
    'uid': 2445590,
    'rcmdReason': ''},
   ...
   {'id': 1401095614,
    'v': 6,
    't': 0,
    'at': 1595912228815,
    'alg': None,
    'uid': 2445590,
    'rcmdReason': ''}],
  'shareCount': 960,
  'commentCount': 285,
  'remixVideo': None,
  'sharedUsers': None,
  'historySharedUsers': None},
 'urls': None,
 'privileges': [{'id': 997889,
   'fee': 8,
   'payed': 0,
   'realPayed': 0,
   'st': 0,
   'pl': 128000,
   'dl': 0,
   'sp': 7,
   'cp': 1,
   'subp': 1,
   'cs': False,
   'maxbr': 999000,
   'fl': 128000,
   'pc': None,
   'toast': False,
   'flag': 324,
   'paidBigBang': False,
   'preSell': False,
   'playMaxbr': 999000,
   'downloadMaxbr': 999000,
   'rscl': None,
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'chargeInfoList': [{'rate': 128000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 192000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1},
    {'rate': 320000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1},
    {'rate': 999000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1}]},
  {'id': 5055353,
   'fee': 8,
   'payed': 0,
   'realPayed': 0,
   'st': 0,
   'pl': 128000,
   'dl': 0,
   'sp': 7,
   'cp': 1,
   'subp': 1,
   'cs': False,
   'maxbr': 320000,
   'fl': 128000,
   'pc': None,
   'toast': False,
   'flag': 0,
   'paidBigBang': False,
   'preSell': False,
   'playMaxbr': 320000,
   'downloadMaxbr': 320000,
   'rscl': None,
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'chargeInfoList': [{'rate': 128000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 192000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1},
    {'rate': 320000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1},
    {'rate': 999000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1}]},
  {'id': 1648643,
   'fee': 0,
   'payed': 0,
   'realPayed': 0,
   'st': 0,
   'pl': 320000,
   'dl': 320000,
   'sp': 7,
   'cp': 1,
   'subp': 1,
   'cs': False,
   'maxbr': 320000,
   'fl': 320000,
   'pc': None,
   'toast': False,
   'flag': 0,
   'paidBigBang': False,
   'preSell': False,
   'playMaxbr': 320000,
   'downloadMaxbr': 320000,
   'rscl': None,
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'chargeInfoList': [{'rate': 128000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 192000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 320000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 999000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1}]},
  {'id': 5051131,
   'fee': 8,
   'payed': 0,
   'realPayed': 0,
   'st': 0,
   'pl': 128000,
   'dl': 0,
   'sp': 7,
   'cp': 1,
   'subp': 1,
   'cs': False,
   'maxbr': 320000,
   'fl': 128000,
   'pc': None,
   'toast': False,
   'flag': 4,
   'paidBigBang': False,
   'preSell': False,
   'playMaxbr': 320000,
   'downloadMaxbr': 320000,
   'rscl': None,
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'chargeInfoList': [{'rate': 128000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 192000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1},
    {'rate': 320000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1},
    {'rate': 999000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1}]},
  {'id': 27599301,
   'fee': 0,
   'payed': 0,
   'realPayed': 0,
   'st': 0,
   'pl': 192000,
   'dl': 192000,
   'sp': 7,
   'cp': 1,
   'subp': 1,
   'cs': False,
   'maxbr': 192000,
   'fl': 192000,
   'pc': None,
   'toast': False,
   'flag': 128,
   'paidBigBang': False,
   'preSell': False,
   'playMaxbr': 192000,
   'downloadMaxbr': 192000,
   'rscl': None,
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'chargeInfoList': [{'rate': 128000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 192000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 320000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 999000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1}]},
  {'id': 5052459,
   'fee': 0,
   'payed': 0,
   'realPayed': 0,
   'st': 0,
   'pl': 320000,
   'dl': 999000,
   'sp': 7,
   'cp': 1,
   'subp': 1,
   'cs': False,
   'maxbr': 999000,
   'fl': 320000,
   'pc': None,
   'toast': False,
   'flag': 128,
   'paidBigBang': False,
   'preSell': False,
   'playMaxbr': 999000,
   'downloadMaxbr': 999000,
   'rscl': None,
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'chargeInfoList': [{'rate': 128000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 192000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 320000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 999000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1}]},
  {'id': 1418454,
   'fee': 8,
   'payed': 0,
   'realPayed': 0,
   'st': 0,
   'pl': 128000,
   'dl': 0,
   'sp': 7,
   'cp': 1,
   'subp': 1,
   'cs': False,
   'maxbr': 320000,
   'fl': 128000,
   'pc': None,
   'toast': False,
   'flag': 4,
   'paidBigBang': False,
   'preSell': False,
   'playMaxbr': 320000,
   'downloadMaxbr': 320000,
   'rscl': None,
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'chargeInfoList': [{'rate': 128000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 192000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1},
    {'rate': 320000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1},
    {'rate': 999000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1}]},
  {'id': 1690717,
   'fee': 0,
   'payed': 0,
   'realPayed': 0,
   'st': 0,
   'pl': 320000,
   'dl': 320000,
   'sp': 7,
   'cp': 1,
   'subp': 1,
   'cs': False,
   'maxbr': 320000,
   'fl': 320000,
   'pc': None,
   'toast': False,
   'flag': 128,
   'paidBigBang': False,
   'preSell': False,
   'playMaxbr': 320000,
   'downloadMaxbr': 320000,
   'rscl': None,
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'chargeInfoList': [{'rate': 128000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 192000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 320000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 999000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1}]},
  {'id': 5040736,
   'fee': 8,
   'payed': 0,
   'realPayed': 0,
   'st': 0,
   'pl': 128000,
   'dl': 0,
   'sp': 7,
   'cp': 1,
   'subp': 1,
   'cs': False,
   'maxbr': 320000,
   'fl': 128000,
   'pc': None,
   'toast': False,
   'flag': 256,
   'paidBigBang': False,
   'preSell': False,
   'playMaxbr': 320000,
   'downloadMaxbr': 320000,
   'rscl': None,
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'chargeInfoList': [{'rate': 128000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 192000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1},
    {'rate': 320000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1},
    {'rate': 999000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1}]},
  {'id': 31152707,
   'fee': 0,
   'payed': 0,
   'realPayed': 0,
   'st': 0,
   'pl': 320000,
   'dl': 320000,
   'sp': 7,
   'cp': 1,
   'subp': 1,
   'cs': False,
   'maxbr': 320000,
   'fl': 320000,
   'pc': None,
   'toast': False,
   'flag': 128,
   'paidBigBang': False,
   'preSell': False,
   'playMaxbr': 320000,
   'downloadMaxbr': 320000,
   'rscl': None,
   'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False},
   'chargeInfoList': [{'rate': 128000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 192000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 320000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 0},
    {'rate': 999000,
     'chargeUrl': None,
     'chargeMessage': None,
     'chargeType': 1}]}],
 'sharedPrivilege': None
 }
```

### User

Verse： https://music.163.com/#/user/home?id=319322859
关注列表: https://music.163.com/#/user/follows?id=319322859

## 爬虫测试

### 获取歌单，专辑列表

```python
import requests
from bs4 import BeautifulSoup

headers = {
    'Referer':'http://music.163.com/',
    'Host':'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
                
play_url = 'http://music.163.com/album?id=2084576'

s = requests.session()
s = BeautifulSoup(s.get(play_url,headers = headers).content)
# main = s.find('table',{'class':'m-table'}) JS渲染，无效
# <ul class="f-hide">
#     <li><a href="/song?id=22712178">Sure As The Sunshine</a></li>
#     <li><a href="/song?id=22712177">春の雪</a></li>
#     <li><a href="/song?id=22712172">Not Enough</a></li>
#     <li><a href="/song?id=22712180">Dans Un Reve</a></li>
#     <li><a href="/song?id=22712174">About Romance</a></li>
#     <li><a href="/song?id=22712176">Love &amp; Positivity</a></li>
#     <li><a href="/song?id=22712173">Refrain</a></li>
#     <li><a href="/song?id=22712179">Starlight</a></li>
#     <li><a href="/song?id=22712182">Utakata</a></li>
#     <li><a href="/song?id=22712175">Children</a></li>
#     <li><a href="/song?id=22712183">Sounds Of Color</a></li>
#     <li><a href="/song?id=22712181">Not Enough -Cradle Orchestra Remix-</a></li>
# </ul>
## 只能获取有版权的歌曲名称与链接
play_infos = s.find('ul',{'class':'f-hide'}) 
for music in play_infos.find_all('a'):
    print('{} : {}'.format(music.text,music['href']))
```

### 使用Mutagen

```python
from mutagen.mp3 import MP3
from urllib.request import urlretrieve

music = apis.track.GetTrackAudio(22712178)

url = music['data'][0]['url']
filename, headers = urlretrieve(url)
audio = MP3(filename)
print(audio.info.length) ## 267.33714285714285 实际4:27，即267
print(audio.filename) ## C:\Users\ADMINI~1\AppData\Local\Temp\tmp7gzde11x 貌似可以获取320kbps高品质音乐，默认下载只有128kbps
print(audio.info.pprint()) ## MPEG 1 layer 3, 320000 bps (CBR), 44100 Hz, 2 chn, 267.34 seconds
```

但上述方法比较慢，且消耗太多资源，我们直接用爬虫爬取网易云渲染后的页面，以http://music.163.com/album?id=2084576为例

```python

```



