from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import ListView

from . import db_queries, models, services


class InputListView(ListView):
    """Get input list"""

    template_name = "main/inputs.html"
    context_object_name = "inputs"
    model = models.Inputs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Список инпутов"
        return context


def create_input_view(request):
    if request.method == 'POST':
        _input = request.POST.get("value")
        services.create_input(_input)
        return HttpResponse()

    last_entry_id = db_queries.get_last_input_id()
    context = {"title": "Создать инпут", "last_entry_id": last_entry_id}
    return render(request, 'main/create_input.html', context=context)
