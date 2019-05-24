from django.contrib import admin
from django.urls import include, path

from . import views
from places.views import get_continents, get_countries, get_cities, create_continent, create_country

urlpatterns = [
	path('', views.index),
    path('admin', admin.site.urls),
    path('continents', get_continents),
    path('countries', get_countries),
    path('cities', get_cities),
    path('createContinent', create_continent),
    path('createCountry', create_country)
]