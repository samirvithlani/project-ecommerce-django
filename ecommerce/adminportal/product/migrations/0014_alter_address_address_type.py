# Generated by Django 4.0.1 on 2022-01-31 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_address_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(default='Home', max_length=10),
        ),
    ]
