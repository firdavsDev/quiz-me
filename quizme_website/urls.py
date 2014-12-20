from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quizme_website.views.home', name='home'),
    # url(r'^quizme_website/', include('quizme_website.foo.urls')),

    url(r'^$', 'questions.views.view_quiz', name='quiz'),
    url(r'^question$', 'questions.views.view_quiz', name='question'),
    url(r'^answer$', 'questions.views.view_quiz', name='question'),
    url(r'^login$', 'emailusername.views.login', name='login'),
    url(r'^logout$', 'emailusername.views.logout', name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
