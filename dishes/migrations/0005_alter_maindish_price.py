# Generated by Django 4.0.3 on 2022-03-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_maindish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindish',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
