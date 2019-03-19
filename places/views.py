from django.shortcuts import render
from django.http import JsonResponse
from places.models import Continent, Country, City
import json

def get_continents(request):
    return JsonResponse([c.to_json() for c in Continent.objects.all()], safe=False)

def get_countries(request):
    return JsonResponse([c.to_json() for c in Country.objects.all()], safe=False)

def get_cities(request):
    return JsonResponse([c.to_json() for c in City.objects.all()], safe=False)

def create_continent(request):
	if request.method == 'POST' and request.POST and request.POST.get('name') and request.POST.get('latitude_center') and request.POST.get('longitude_center'):
		name = request.POST.get('name')
		lat_center = float(request.POST.get('latitude_center'))
		long_center = float(request.POST.get('longitude_center'))
		new_continent = Continent.objects.create(name=name, latitude_center=lat_center, longitude_center=long_center)
		return JsonResponse(new_continent.to_json(), safe=False)
	else:
		return JsonResponse({'message': 'must include continent name, latitude, and longitude'}, status=400, safe=False)

def create_country(request):
	if request.method == 'POST' and request.POST and request.POST.get('name') and request.POST.get('latitude_center') and request.POST.get('longitude_center') and request.POST.get('continent_id'):
		name = request.POST.get('name')
		lat_center = float(request.POST.get('latitude_center'))
		long_center = float(request.POST.get('longitude_center'))
		continent_id = int(request.POST.get('continent_id'))
		try:
			continent = Continent.objects.get(id=continent_id)
		except:
			return JsonResponse({'message': 'continent id was not found'}, status=404, safe=False)

		new_country = Country.objects.create(continent=continent, name=name, latitude_center=lat_center, longitude_center=long_center, basic_info="country filler text")
		return JsonResponse(new_country.to_json(), safe=False)
	else:
		return JsonResponse({'message': 'must include continent id as well as country name, latitude, and longitude'}, status=400, safe=False)


























