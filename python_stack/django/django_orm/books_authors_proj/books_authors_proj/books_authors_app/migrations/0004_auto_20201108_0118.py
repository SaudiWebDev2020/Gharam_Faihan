# Generated by Django 2.2.4 on 2020-11-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_auto_20201104_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='book',
            field=models.ManyToManyField(related_name='authors', to='books_authors_app.Books'),
        ),
    ]
