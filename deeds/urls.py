from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from deeds import views
from rest_framework.authtoken import views as rest_auth_views

urlpatterns = [
    url(r'^api/token-auth/$', rest_auth_views.obtain_auth_token),
	url(r'^api/deeds/$', views.DeedList.as_view()),
	url(r'^api/deeds/(?P<pk>[0-9]+)/$', views.DeedDetail.as_view()),
	url(r'^api/pledges/$', views.PledgeList.as_view()),
	]

urlpatterns = format_suffix_patterns(urlpatterns)