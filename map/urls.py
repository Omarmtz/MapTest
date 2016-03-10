from django.conf.urls import url,include
from . import views

urlpatterns = [
    #url(r'^$', views.MapPoints.as_view(), name='map'),
    url(r'^test', views.Test.as_view(), name='gettest'),
    url(r'^$', views.Index.as_view(), name='index'),

]
