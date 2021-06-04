from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('song/', views.netease_infos, name='netease_infos_name'),
]
