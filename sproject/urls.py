from django.conf.urls import patterns, include, url

from django.contrib import admin
import scontacts.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', scontacts.views.ListContactView.as_view(),
        name='contacts-list',),    
)
