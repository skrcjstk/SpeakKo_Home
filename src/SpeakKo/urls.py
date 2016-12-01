from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views
import debug_toolbar

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^lookaround/$', views.LookAroundPage.as_view(), name='lookaround'),

    url(r'^course/', include('course.urls', namespace='course')),

	#url(r'^courseall/$', views.CourseAllPage.as_view(), name='courseall'),
	url(r'^content/$', views.ContentPage.as_view(), name='content'),
	url(r'^teacher/$', views.TeacherPage.as_view(), name='teacher'),

    url(r'^registration/$', views.RegistrationPage.as_view(), name='registration'),
    url(r'^leveltest/$', views.LevelTestPage.as_view(), name='leveltest'),
    url(r'^tuition/$', views.TuitionPage.as_view(), name='tuition'),

    url(r'^notification/$', views.NotificationPage.as_view(), name='notification'),
    url(r'^event/$', views.EventPage.as_view(), name='event'),
    url(r'^faq/$', views.FAQPage.as_view(), name='faq'),
    url(r'^inquiry/$', views.InquiryPage.as_view(), name='inquiry'),

	url(r'^about/$', views.AboutPage.as_view(), name='about'),

    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
