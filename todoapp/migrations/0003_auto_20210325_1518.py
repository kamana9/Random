# Generated by Django 3.1.7 on 2021-03-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20210325_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
