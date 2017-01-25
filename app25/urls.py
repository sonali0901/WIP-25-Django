from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views

urlpatterns = [

    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/favourities/(?P<pk>\d+)/$',views.add_fav,name='add_fav'),
    url(r'^accounts/register/$',views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete,name='registration_complete'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
]
