from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView
from django.conf.urls import handler404
handler404 = 'cms.views.handler404'



urlpatterns = [
    url(r'^$', views.index_handler),
    url(r'get_my_please_pages/',views.get_my_please_pages),
    url(r'get_pages/', views.get_pages),
    url(r'category1/', views.category1),
    url(r'category2/', views.category2),
    url(r'getcategory/', views.getcategory),
    url(r'get_level_category/', views.get_level_category),
    url(r'get_data_map/', views.get_data_map),
    url(r'raiting/', views.raiting),
    url(r'get_data_fortemplate/', views.fortemplate),
    url(r'search_helper/', views.search_helper),
    url(r'FAQs/', views.FAQs),
    url(r'Encyclopedia_of_knowledge/', views.Encyclopedia),
    url(r'get_client_ip/', views.get_client_ip),
    url(r'get_girls/', views.get_girls),
    url(r'search_ajax/', views.search_ajax),
    url(r'widget_form_connect_with_us/', views.widget_form_connect_with_us),
    url(r'counter_children/', views.counter_children),
    url(r'load_my_map_please/', TemplateView.as_view(template_name='widget/map_widget/map.html')),
    url(r'(?P<type>[-\w]+)/(?P<slug>[-\w]+)/(?P<id>\d+)/$', views.razdel_handler, name='razdel-handler'),
    url(r'', include('feincms.urls')),
]
