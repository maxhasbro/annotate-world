from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
	path('', views.index),
    path('places', include('places.urls')),
    path('admin', admin.site.urls),
]