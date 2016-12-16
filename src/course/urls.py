from django.conf.urls import url
from . import views

app_name = 'course'

urlpatterns = [
    # /course/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/$', views.CategoryView.as_view(), name='category'),
    url(r'^teacher/$', views.TeacherIndexView.as_view(), name='teacher'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<class_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^login/$', views.LoginView.as_view(), name="login"),
]