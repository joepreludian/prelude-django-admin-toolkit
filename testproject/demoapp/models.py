from django.db import models
from django_quill.fields import QuillField


class TimeCapsule(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True)
    age = models.IntegerField(help_text='< 0; Before Christ')
    current_date = models.DateField(null=True)
    current_datetime = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    time_capsule = models.ForeignKey('demoapp.TimeCapsule', on_delete=models.CASCADE, null=True, blank=False)
    name = models.CharField(max_length=32)
    item_no = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'{self.name}'


class ExtraItems(models.Model):
    name = models.CharField(max_length=22)

    def __str__(self):
        return f'{self.name}'


class QuillEditor(models.Model):

    SIMPLE_CHOICES = (
        (0, 'Choice1'),
        (1, 'Choice2'),
        (2, 'Choice3'),
        (3, 'Choice4')
    )

    title = models.CharField(max_length=196, help_text='Title Help Text')
    json_data = models.JSONField()
    editor = QuillField(help_text='Help text')
    datetime = models.DateTimeField(null=True)
    date = models.DateField(null=True)
    textarea = models.TextField(null=True)
    simple_choices = models.PositiveIntegerField(choices=SIMPLE_CHOICES, null=True)
    integer_field = models.PositiveIntegerField(null=True)
    item_fk = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL, help_text='Item FK')
    checkbox = models.BooleanField(default=True, null=True, help_text='Checkbox With helptext')
    checkbox2 = models.BooleanField(default=False)