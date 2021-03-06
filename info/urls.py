from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PageView.as_view(), name='home'),
    url(r'^contact/$', views.contactView, name='contact'),
    url(r'^thanks/$', views.contactView, name='thanks'),
    url(r'^news/$', views.NewsView.as_view(), name='news'),
    url(r'^search/$', views.search, name='search'),
    url(r'^page/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),
]