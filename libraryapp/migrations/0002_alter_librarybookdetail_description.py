# Generated by Django 5.0.6 on 2024-06-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarybookdetail',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
