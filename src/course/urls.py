from django.conf.urls import url
from . import views



urlpatterns = [
    # /course/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #url(r'^(?P<class_id>[0-9]+)/$', views.detail, name='detail'),



    #url(r'^login/$', views.LoginView.as_view(), name="login"),

]