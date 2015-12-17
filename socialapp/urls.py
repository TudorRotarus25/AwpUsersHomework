from django.conf.urls import url
from socialapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_details, name='post_details'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile_payload, name='view_profile_payload'),
]

urlpatterns += staticfiles_urlpatterns()
