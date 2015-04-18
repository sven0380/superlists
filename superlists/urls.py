from django.conf.urls import patterns, include, url
from lists import urls

urlpatterns = patterns('',
                       url(r'^$', 'lists.views.home_page', name='home'),
                       url(r'^lists/', include('lists.urls')),
                       # url(r'^admin/', include(admin.site.urls)),
)