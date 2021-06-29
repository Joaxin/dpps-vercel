from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('tools/', views.music_url_tools, name = "music_url_tools"),
    path('netease/', views.netease_infos, name='netease_infos_name'),
]
