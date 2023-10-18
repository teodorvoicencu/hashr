from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email", "created_at", "updated_at"]
    search_fields = ["id", "first_name", "last_name", "email"]
    ordering = ["updated_at"]
