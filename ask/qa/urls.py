"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^test/$', views.test),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.test, name='login'),
    url(r'^signup/$',views.test, name='signup'),
    url(r'^logout/', views.test, name='logout'),
    url(r'^question/(?P<pk>\d+)/$',views.detail, name='question_detail'),
    url(r'^answer/', views.test, name='question_answer'),
    url(r'ask/.*$',views.test, name='question_ask'),
    url(r'popular/$',views.popular, name='popular'),
    url(r'^new/$', views.test, name='new'),
]