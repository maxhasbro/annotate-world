from django.http import HttpResponse

def index(request):
    return HttpResponse("<h3>Hello, map lovers! This is the homepage</h3>")