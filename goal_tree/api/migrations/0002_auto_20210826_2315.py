# Generated by Django 3.2.4 on 2021-08-27 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='tree',
            name='numchild',
        ),
        migrations.RemoveField(
            model_name='tree',
            name='path',
        ),
    ]
