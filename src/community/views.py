from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from . import models
from django.template import loader
from .models import Notification

# Create your views here.

class NotificationView(generic.TemplateView):
	template_name = "community/notification.html"
	def getqueryset(self):
		return Notification.objects.all()
