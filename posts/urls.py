from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^feeds/$',views.feeds,name='allImages'),
    url(r'^profile/$',views.profile,name = 'NewProfile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^image/(\d+)',views.image,name ='image'),
    # url(r'^search/', views.search_results, name='search_results')
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)   