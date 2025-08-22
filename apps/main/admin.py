from django.contrib import admin

from apps.main.models import Inputs


@admin.register(Inputs)
class InputsAdmin(admin.ModelAdmin):
    list_display = ("id", "input_field")
    list_display_links = ("id", "input_field")
    search_fields = ("id", )
    list_max_show_all = 10
    list_per_page = 15
    ordering = ["-id"]
    