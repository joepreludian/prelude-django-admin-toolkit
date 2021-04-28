from django.contrib import admin
from demoapp.models import TimeCapsule, Item, ExtraItems, QuillEditor

from prelude_django_admin_toolkit.admin import site as prl_admin
from prelude_django_admin_toolkit import forms
from prelude_django_admin_toolkit.admin import PrlModelAdmin


@admin.register(TimeCapsule, site=prl_admin)
class TimeCapsuleAdmin(PrlModelAdmin):

    #form = forms.PrlModelForm

    list_display = ['name', 'age', 'current_date']

    list_filter = ['current_date', 'age']
   
    # @todo FIX date_hierarchy widget 
    date_hierarchy = 'current_date'
    
    search_fields = ('name', )

    fieldsets = (
        (None, {
            'fields': ('name', 'current_date', 'current_datetime')
        }),
        ('Subsection', {
            'fields': ('description',)
        }),
        ('Advanced section', {
            'classes': ('collapse', 'tab'),
            'description': 'A simple description',
            'fields': ('age',),
        }),
    )


@admin.register(Item, site=prl_admin)
class ItemAdmin(PrlModelAdmin):
    list_display = ['name', 'item_no']
    
    list_filter = ['time_capsule']


@admin.register(ExtraItems, site=prl_admin)
class ExtraItemsAdmin(PrlModelAdmin):
    pass


@admin.register(QuillEditor, site=prl_admin)
class QuillAdmin(PrlModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'title', ('datetime', 'date'),
                'editor',
                'json_data',
                ('simple_choices', 'integer_field'),
                'item_fk')
        }),
    )