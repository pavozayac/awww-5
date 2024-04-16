from django.shortcuts import render
# from django.http import HttpResponse
# fromdjango.template import Context
from .models import Picture


def index(req):
    return render(req, 'pictures.html', context={
        "pictures": Picture.objects.all(),
        "auth": req.user.is_authenticated,
    })


def picture(req, id):
    picture = Picture.objects.prefetch_related('rectangles').get(id=id)
    return render(req, 'picture.html', context={
        "picture": picture,
        "rectangles": picture.rectangles.all(),
        "auth": req.user.is_authenticated,
    })