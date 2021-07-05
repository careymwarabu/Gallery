from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_results, name='search_results'),
    re_path('image/(?P<image_id>\d+)', views.view_image, name='image'),
    re_path('category/(?P<category_id>\d+)', views.get_category, name='category'),
    re_path('location/(?P<location_id>\d+)', views.get_location, name='location'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
