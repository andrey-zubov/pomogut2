from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from feincms.module.page.sitemap import PageSitemap
from django.conf.urls import handler404
handler404 = 'cms.views.handler404'

admin.autodiscover()


urlpatterns = [
    url(r'^$', include('MainPagePomogut.MainPagePomogut_urls')),
    url(r'add_the_information/', include('MainPagePomogut.MainPagePomogut_urls')),
    url(r'^pomog/', include('cms.cms_urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('feincms.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)