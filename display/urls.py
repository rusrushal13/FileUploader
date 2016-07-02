
from django.conf.urls import url
from . import views

app_name = 'display'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name ='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name ='details'),
    url(r'^add/$', views.FileCreate.as_view(), name='file-add'),

]