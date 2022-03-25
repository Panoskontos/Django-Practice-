# Generated by Django 4.0.3 on 2022-03-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0010_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('Out for Delivery', 'Out for Delivery'), ('Delivered', 'delivered')], max_length=100)),
            ],
        ),
    ]
