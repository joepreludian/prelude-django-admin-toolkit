# Generated by Django 3.1.1 on 2020-10-12 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='time_capsule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demoapp.timecapsule'),
        ),
    ]
