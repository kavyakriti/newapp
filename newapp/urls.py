"""newapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from newsblog import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'newsblog'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',v.index),
    url(r'^mainpg/',v.mainpg),
    url(r'^register/',v.register),
    url(r'^login/',v.login_request),
    url(r'^business/',v.business), 
    url(r'^technical/',v.technical),
    url(r'^international/',v.international),
    url(r'^entertainment/',v.entertainment),
    url(r'^sports/',v.sports), 
    url(r'^search/', v.search, name="search"),
    url(r'^logout/',v.logout_request),
   
]


urlpatterns += staticfiles_urlpatterns()

