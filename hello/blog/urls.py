from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',views.blog_index,name='blog_index'),

    path('<int:pk>', views.blog_detail, name='blog_detail'),
    path('<category>',views.blog_category,name='blog_category'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)