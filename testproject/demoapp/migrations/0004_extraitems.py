# Generated by Django 3.1.5 on 2021-03-15 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_auto_20201013_0338'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=22)),
            ],
        ),
    ]
