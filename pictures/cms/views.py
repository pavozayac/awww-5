from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from .forms import RectangleForm
# from django.http import HttpResponse
# fromdjango.template import Context
from .models import Picture, Rectangle


def index(req):
    pics = Picture.objects.prefetch_related('rectangles').all()
    paginator = Paginator(pics, 10)

    page_number = req.GET.get("page")
    page = paginator.page(page_number if page_number is not None else 1)

    return render(req, 'pictures.html', context={
        "pics_page": page,
        "auth": req.user.is_authenticated,
    })


def picture(req, id):
    picture = Picture.objects.prefetch_related('rectangles').get(id=id)

    if req.method == 'POST':
        form = RectangleForm(req.POST)
        rect = form.save(commit=False)

        rect.picture_id = id

        if form.is_valid():
            rect.save()

            # picture.rectangles.add(form.instance)

            return redirect(f'/cms/{id}')
    else:
        form = RectangleForm()

    return render(req, 'picture.html', context={
        "picture": picture,
        "rectangles": picture.rectangles.all(),
        "auth": req.user.is_authenticated,
        "form": form,
    })


def delete_rectangle(req, picture_id, rect_id):
    rect = Rectangle.objects.get(id=rect_id)
    rect.delete()

    return redirect(f'/cms/{picture_id}')
    