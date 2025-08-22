from django.urls import path

from . import views

urlpatterns = [
    path("", views.create_input_view, name="create-input"),
    path("inputs/", views.get_input_list_view, name='input-list')
]
