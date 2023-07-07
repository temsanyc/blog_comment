from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.word_home,name='home'),
    path('detail/', views.word_detail,name='detail'),
    path('index/',views.word_index, name='index'),
    path('<int:pk>', views.MoreDetailView.as_view(), name='more_detail')



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)