from django.urls import path

from .views import InputListView, create_input_view

urlpatterns = [
    path("", create_input_view, name="create-input"),
    path("inputs/", InputListView.as_view(), name='input-list')
]
