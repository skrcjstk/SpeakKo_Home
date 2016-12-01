from django.views import generic
from django.http import HttpResponse
#from django.contrib.auth import get_user_model
from . import models
from django.template import loader


from .models import Subject


def index(request):
    all_subject = Subject.objects.all()
    template =loader.get_template('course/index.html')
    context = {'all_subject': all_subject}



    #for subject in all_subject:
    #    url = '/course/' + str(subject.id) + '/'
    #    html += '<a href="' + url + '">' + subject.class_title + '</a><br>'
    return HttpResponse(template.render(context, request))






class IndexView(generic.TemplateView):
    template_name = "course/index.html"
    #def get_queryset(self):
    #    return BaseCourse.objects.all()

#def detail(request, class_id):
#    return HttpResponse("<h2> Details for Class id: " + str(class_id) + " </h2>")

class DetailView(generic.TemplateView):
#    #model = BaseCourse
    template_name = 'course/detail.html'