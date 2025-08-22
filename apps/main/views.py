from django.shortcuts import render
from django.http.response import HttpResponse

from . import db_queries, services


def get_input_list_view(request) -> None:
    """Get input list"""

    inputs = services.get_input_list()
    context = {"title": "Список инпутов", "inputs": inputs}
    return render(request, "main/inputs.html", context=context)


def create_input_view(request):
    if request.method == 'POST':
        _input = request.POST.get("value")
        services.create_input(_input)
        return HttpResponse()

    last_entry_id = db_queries.get_last_input_id()
    context = {"title": "Создать инпут", "last_entry_id": last_entry_id}
    return render(request, 'main/create_input.html', context=context)
