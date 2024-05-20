from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from .forms import PictureFilterForm, RectangleForm
# from django.http import HttpResponse
# fromdjango.template import Context
from .models import Picture, Rectangle


def index(req):
    pics = Picture.objects.prefetch_related('rectangles').all()

    sort_date = req.GET.get('sort_date')
    tags = req.GET.get('filter_tags')
    
    if sort_date is not None:
        if sort_date == 'asc':
            pics = pics.order_by('date_added')
        else:
            pics = pics.order_by('-date_added')

    if tags is not None:
        for tag in tags.split(','):
            pics = pics.filter(tags__contains=tag)
    
    
    paginator = Paginator(pics, 10)

    page_number = req.GET.get('page')
    page = paginator.page(page_number if page_number is not None else 1)

    return render(req, 'pictures.html', context={
        "pics_page": page,
        "auth": req.user.is_authenticated,
        "form": PictureFilterForm(),
    })


def picture(req, id):
    picture = Picture.objects.prefetch_related('rectangles').get(id=id)

    if req.method == 'POST':
        form = RectangleForm(req.POST)
        rect = form.save(commit=False)

        rect.picture_id = id

        if form.is_valid():
            rect.save()

            return redirect('picture', id=id)
    else:
        form = RectangleForm()

    return render(req, 'picture.html', context={
        "picture": picture,
        "auth": req.user.is_authenticated,
        "form": form,
    })


def delete_rectangle(req, picture_id, rect_id):
    rect = Rectangle.objects.get(id=rect_id)
    rect.delete()

    return redirect('picture', id=picture_id)
    