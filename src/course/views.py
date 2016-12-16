from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Subject
from .models import Teacher


class IndexView(generic.ListView):
    template_name = "course/index.html"
    context_object_name = "all_subjects"
    def get_queryset(self):
        return Subject.objects.order_by('class_level')
        #return Subject.objects.all()

class DetailView(generic.DeleteView):
    model = Subject
    template_name = 'course/detail.html'


class CategoryView(generic.ListView):
    template_name = "course/category.html"
    context_object_name = "all_subjects"
    def get_queryset(self):
        return Subject.objects.order_by('class_category')
        #return Subject.objects.all()


class TeacherIndexView(generic.ListView):
    template_name = "course/teacher.html"
    context_object_name = "all_teachers"
    def get_queryset(self):
        return Teacher.objects.all()












    # from django.shortcuts import render, get_object_or_404

    # def index(request):
    #    all_subject = Subject.objects.all()
    #    context = {'all_subject': all_subject}
    #    return render(request, 'course/index.html', context)

    # def detail(request, class_id):
    #    subject = get_object_or_404(Subject, pk=class_id) # class id 가 없으면 error messaage 띄움
    #    return render(request, 'course/detail.html', {'subject': subject})
