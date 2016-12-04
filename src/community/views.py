from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from . import models
from django.template import loader
from .models import Notification

# Create your views here.

class NotificationView(generic.ListView):
	template_name = "community/notification.html"
	def get_queryset(self):
		return Notification.objects.all()
