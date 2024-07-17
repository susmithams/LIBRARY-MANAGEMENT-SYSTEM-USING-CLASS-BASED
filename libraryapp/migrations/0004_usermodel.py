# Generated by Django 5.0.6 on 2024-06-07 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='usermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('job', models.CharField(max_length=40)),
                ('higher_qualification', models.CharField(max_length=50)),
            ],
        ),
    ]
