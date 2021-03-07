"""python_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_song/', views.SongAPI.as_view(),  name='add_song'),
    path('get_song/<int:id>/', views.SongAPI.as_view(),  name='get_song'),
    path('delete_song/<int:id>/', views.SongAPI.as_view(),  name='delete_song'),
    path('update_song/<int:id>/', views.SongAPI.as_view(),  name='update_song'),
]
