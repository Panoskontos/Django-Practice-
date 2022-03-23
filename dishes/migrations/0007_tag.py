# Generated by Django 4.0.3 on 2022-03-23 20:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0006_alter_salad_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]