from django.contrib import admin

from .models import Birthday


admin.site.empty_value_display = 'Не задано'


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'birthday',
        'image',
    )

    edit_display = (
        'id',
        'first_name',
        'last_name',
        'birthday',
        'image',
    )

    search_fields = ('birthday',)
    list_display_links = ('id',)


admin.site.register(Birthday, BirthdayAdmin)
