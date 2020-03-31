# Generated by Django 3.0.4 on 2020-03-31 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20200330_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='attributes',
        ),
        migrations.AlterField(
            model_name='author',
            name='affiliation',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterModelTable(
            name='author',
            table='Authors',
        ),
    ]
