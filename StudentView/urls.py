from . import views
from django.urls import path

urlpatterns = [
    path("add_manually_post", views.add_manually_post, name="add_manually_post"),
    path("submitted", views.submitted, name="submitted"),
]
