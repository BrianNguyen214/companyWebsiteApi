from django.conf.urls import url
from rest_framework import serializers, viewsets, routers
#from .views import MemberRUDView, MemberAPIView, test
from .views import MembersManip

urlpatterns = [
    #url(r'^(?P<pk>\d+)/$', MemberRUDView.as_view(), name='member-rud'),
    url(r'^$', MembersManip, name='members'),
    #url(r'^$', MemberAPIView.as_view(), name='post-create'),
    #url(r'allmembers/', MemberRUDView.as_view(), name='member-rud'),
]
