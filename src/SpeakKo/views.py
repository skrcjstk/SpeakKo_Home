from django.views import generic

class HomePage(generic.TemplateView):
    template_name = "home.html"
class LookAroundPage(generic.TemplateView):
    template_name = "lookaround.html"

class CourseAllPage(generic.TemplateView):
    template_name = "course/courseall.html"
class ContentPage(generic.TemplateView):
    template_name = "course/content.html"
class TeacherPage(generic.TemplateView):
    template_name = "course/teacher.html"

class RegistrationPage(generic.TemplateView):
    template_name = "courseRegistration/registration.html"
class LevelTestPage(generic.TemplateView):
    template_name = "courseRegistration/leveltest.html"
class TuitionPage(generic.TemplateView):
    template_name = "courseRegistration/tuition.html"

class NotificationPage(generic.TemplateView):
    template_name = "community/notification.html"
class EventPage(generic.TemplateView):
    template_name = "community/event.html"
class FAQPage(generic.TemplateView):		
    template_name = "community/faq.html"
class InquiryPage(generic.TemplateView):
    template_name = "community/inquiry.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"
