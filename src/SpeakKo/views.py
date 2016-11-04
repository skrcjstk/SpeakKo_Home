from django.views import generic

class HomePage(generic.TemplateView):
    template_name = "home.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class LevelTestPage(generic.TemplateView):
    template_name = "leveltest.html"

class CoursePage(generic.TemplateView):
    template_name = "course.html"

class RegistrationPage(generic.TemplateView):
    template_name = "registration.html"
