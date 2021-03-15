from django.db import models


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
