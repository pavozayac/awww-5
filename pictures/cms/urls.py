from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.picture, name="picture"),
    path("<int:id>/", views.picture, name="picture"),
    path("<int:picture_id>/<int:rect_id>/delete", views.delete_rectangle, name="delete_rectangle"),
    # path("<int:picture_id>/add", views.add_rectangle, name="delete_rectangle"),
]
