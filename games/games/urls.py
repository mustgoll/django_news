"""games URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from gamelives import views
from django.views.decorators.cache import cache_page
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.home),
    url(r'^news/$',cache_page(60 * 15)(views.news)),
    url(r'^sina/$', views.sina),
    url(r'^acfun/$', views.acfun),
    url(r'^lives/$', views.lives),
    url(r'^yzm/(\d*)$', views.yzm),
    url(r'^logout/$', views.logout),
    url(r'^login/(?P<type>\d*)$', views.login),
    url(r'^$', views.home)

]



