from django.http import HttpResponse


def index(request):
    return HttpResponse("Здесь что-то должно быть")

