# Generated by Django 5.0.6 on 2024-06-10 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0008_remove_acceptedbooks_request_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acceptedbooks',
            name='book',
        ),
        migrations.RemoveField(
            model_name='acceptedbooks',
            name='user',
        ),
        migrations.AddField(
            model_name='acceptedbooks',
            name='details',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='libraryapp.bookrequest'),
            preserve_default=False,
        ),
    ]
