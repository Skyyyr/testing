from django.http import HttpResponse


def home(request):
    page = open('static/index.html').read()
    return HttpResponse(page)