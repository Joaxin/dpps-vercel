以Haruka Nakamura - Twilight为例：
```html
<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=22701029&auto=0&height=66"></iframe>
```

<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=22701029&auto=0&height=66"></iframe>

frameborder:

border:

marginwidth/marginheight:

width/height: iframe宽度和高度

auto: 0为非自动播放，1为自动播放

## 网易云链接

PC客户端: 

以歌曲Andrea Bocelli/Sarah Brightman - Time To Say Goodbye (Con Te Partirò)和专辑阿南亮子- Eternal Light为例：

```
http://music.163.com/song?id=16323601&userid=XXXXXX
http://music.163.com/song?id=16323601
https://music.163.com/#/song?id=16323601

https://music.163.com/#/album?id=2084576
https://music.163.com/album?id=2084576

网页端超过20首会显示 查看更多内容，请下载客户端
https://music.163.com/#/playlist?id=5272670909
https://music.163.com/playlist?id=5272670909
自己歌单需登录: https://music.163.com/#/my/m/music/playlist?id=XXXX
```

移动端

```python
https://music.163.com/m/song?id=16323601&userid=XXXXXX&from=timeline&isappinstalled=0
# timeline：朋友圈 APP 是否安装（is app installed）
https://y.music.163.com/m/song?id=16323601
分享Andrea Bocelli/Sarah Brightman的单曲《Time To Say Goodbye (Con Te Partirò)》: https://y.music.163.com/m/song/16323601/?userid=XXXXXX&app_version=7.3.28 (来自@网易云音乐)

https://y.music.163.com/m/song?id=16323601&uct=5rWe9qDpKcHMjsbB6LxZwQ%253D%253D&app_version=8.2.31&sc=wm
// 最新版的userid已加密
```

新浪微博(暂不支持)

```
https://music.163.com/#/share/sina/direct/18/16323601?userid=XXXXXX&haspic=0
```

> 如果用户没有在客户端登录（“游客”），那分享链接虽然依旧会包含一个“userid”，但是无效，会指向404网页。
>
> 歌曲id前面的数字 18 表示分享的音频的类型。18表示单曲，19表示专辑，17 表示节目。

用户链接

```
https://music.163.com/#/user/home?id=XXXXXX
```
