# Generated by Django 2.2.4 on 2020-11-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_auto_20201103_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='old dojo'),
            preserve_default=False,
        ),
    ]