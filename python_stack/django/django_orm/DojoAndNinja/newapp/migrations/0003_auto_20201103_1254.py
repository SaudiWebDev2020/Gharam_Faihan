# Generated by Django 2.2.4 on 2020-11-03 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20201103_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninja',
            old_name='name',
            new_name='dojo_id',
        ),
    ]
