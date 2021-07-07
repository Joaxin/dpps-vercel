from django.urls import path
from . import views

urlpatterns = [
    path('s/', views.netease_song, name = "netease_song"),
    path('al/', views.netease_album, name = "netease_album"),
    path('tools/', views.music_url_tools, name = "music_url_tools"),
    path('s/netease/', views.netease_infos_song, name='netease_infos_song_name'),
    path('al/netease/', views.netease_infos_album, name='netease_infos_album_name'),
]
