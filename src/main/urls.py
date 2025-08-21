from django.urls import path

from .views import InputList, create_input

urlpatterns = [
    path("", create_input, name="create-input"),
    path("inputs/", InputList.as_view(), name='input-list')
]
