from django.contrib import admin
from demoapp.models import TimeCapsule, Item

from prelude_django_admin_toolkit.admin import site as prl_admin
from prelude_django_admin_toolkit import forms
from prelude_django_admin_toolkit.admin import PrlModelAdmin

@admin.register(TimeCapsule, site=prl_admin)
class TimeCapsule(PrlModelAdmin):

    form = forms.PrlModelForm

    list_display = ['name', 'age', 'current_date']

    list_filter = ['current_date', 'age']
    
    search_fields = ('name', )

    fieldsets = (
        (None, {
            'fields': ('name', 'current_date', 'current_datetime')
        }),
        ('Subsection', {
            'fields': ('description',)
        }),
        ('Advanced section', {
            'classes': ('collapse',),
            'fields': ('age',),
        }),
    )


@admin.register(Item, site=prl_admin)
class Item(PrlModelAdmin):
    list_display = ['name', 'item_no', 'time_capsule']
