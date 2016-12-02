from django.conf.urls import url
from . import views
from django.views import generic

app_name = 'community'


urlpatterns = [
	url(r'^$', views.NotificationView.as_view(), name='notification'),
]